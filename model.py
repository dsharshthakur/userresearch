import streamlit as st 
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory
from langchain_google_genai import GoogleGenerativeAI


# load the keyl
key = st.secrets["PROJECT_KEY"] 


def model_config(model, api_key):
    # llm - gemini
    llm = GoogleGenerativeAI(model=model, google_api_key=api_key)
    
    template = '''
     You're Harsh, assuming the role of a researcher at at Insightify Research Co.., tasked with conducting user research interviews.
     Your goal is to ask open-ended questions based on the user's responses, maintaining a human-like interaction 
     without revealing the scripted nature of the prompt. Remember not to disclose that you're an AI bot or a computer program.
     your persona is that of a genuine employee. Let's keep the conversation authentic and concise.
     {history}
     User :{input}
     AI : 
     '''

    # Prompt Template
    prompt = PromptTemplate(input_variables=["history", "inputs"], template=template)
    
    # Chat Memory
    memory = ConversationBufferWindowMemory(k=4)
    chain = ConversationChain(llm=llm, prompt=prompt, memory=memory)
    # Chaining 
    return chain

# Model Object
model = model_config(model="gemini-pro", api_key=key)
