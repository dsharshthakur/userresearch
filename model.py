from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("GOOGLE_API")


def model_config(model, api_key):
    llm = GoogleGenerativeAI(model=model, google_api_key=api_key)
    # template = '''You ron Harsh and you need to act as employee of a company conducting user research interviews.
    # As a User Research Interviewer you need to ask open-ended questions based on the user's responses and
    # ensure that your resonse should feels human-like without revealing the prompt.
    # Don't reveal that you are a AI bot you need to act as a employee
    # of a company.Take any random company name.Keep the conversation as real and short.
    # {history}
    # user : {input}
    # AI :
    #  '''

    template = '''
     You're Harsh, assuming the role of a researcher at userlogy, tasked with conducting user research interviews.
     Your goal is to ask open-ended questions based on the user's responses, maintaining a human-like interaction 
     without revealing the scripted nature of the prompt. Remember not to disclose that you're an AI bot or a computer program.
     your persona is that of a genuine employee. Let's keep the conversation authentic and concise.
     {history}
     User :{input}
     AI : 
     '''


    prompt = PromptTemplate(input_variables=["history", "inputs"], template=template)
    memory = ConversationBufferWindowMemory(k=4)

    chain = ConversationChain(llm=llm, prompt=prompt, memory=memory)

    return chain


model = model_config(model="gemini-pro", api_key=key)
