import streamlit as st
from streamlit_chat import message
from model import model

# Title
st.markdown("<h2 style = 'font-family:system-ui'><span style='color:#0F89B0'>Converse:</span> The User Research Dialogue Tool</h2>",unsafe_allow_html= True)

# Session State for Home-page
if "homepage" not in st.session_state:
    st.session_state["homepage"] = True

# Creating Home Page content for Home-page
def home():
    st.session_state["homepage"] = True

    placeholder = st.empty()

    with placeholder.container():
        st.markdown('<br>', unsafe_allow_html=True)

        st.write("""
        <h5 style = 'font-family:system-ui'>Welcome to the User Research Interview<h5>
        <p style = 'font-family:system-ui'>    
        Thank you for participating in our user research interview! This chatbot is designed to gather valuable insights from you about your experiences and preferences.
        Your feedback will help us improve  our products and services to better meet your needs.
        
        <p style = 'font-family:system-ui'>During this interview, feel free to express your thoughts, opinions, and suggestions openly.
         The chatbot will guide you through a series of questions and prompts, and your responses will be recorded anonymously.</p>

        <p style = 'font-family:system-ui'>Your input is highly valued and appreciated. Let's get started by clicking the "Start" button below.</p>

    """, unsafe_allow_html=True)

        st.markdown('<br>', unsafe_allow_html=True)
        
        # start button
        col1, col2, col3 = st.columns(3)
        with col2:
            start_btn = st.button("Start",use_container_width=True)
            st.session_state["start_btn_active"] = False
            
            # if start button is active
            if start_btn:
                st.session_state["start_btn_active"] = True
                placeholder.empty()

    st.session_state["chat_history"] = []


if st.session_state["homepage"]:
    home()

# Function to get AI response
def get_response(model, user_input):
    response = model.invoke(user_input)
    return response["response"]


if st.session_state["start_btn_active"] == True:
    # Introduction AI Message
    answer = get_response(model, "Introduce Yourself.")
    st.session_state["chat_history"].append({"role": "ai", "message": answer})

    st.session_state["homepage"] = False
    st.session_state["start_btn_active"] = False

if st.session_state["homepage"] == False:
  
    # Conversation Clear/ Leave - Button
    col1,col2 ,col3 = st.columns(3)
    with col3:
        placeholder = st.empty()
        leave_btn = placeholder.button("Leave conversation")
    
    if leave_btn == False:
        # User Message
        user_input = st.chat_input("Enter your message here..")
        
        if user_input:
            # AI Message
            answer = get_response(model, user_input)
            
            #Add the conversation in the session state
            st.session_state["chat_history"].append({"role": "user", "message": user_input})
            st.session_state["chat_history"].append({"role": "ai", "message": answer})

        i = 0
        for chain in st.session_state["chat_history"]:
            # user previous messages
            if chain["role"] == "user":
                message(chain["message"], is_user=True, avatar_style="open-peeps", key=f"user_msg_{i}")
            # AI previous messagea
            else:
                message(chain["message"], is_user=False, avatar_style="fun-emoji", key=f"ai_msg_{i}")

            i = i + 1
    else:
        
        # Clear conversation
        placeholder.empty()

        #Create content for Home Page Again
        st.session_state["homepage"] = True
        home()
