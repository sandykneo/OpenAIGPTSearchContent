import os
import streamlit as st
import openai
from streamlit_chat import message
from langchain_community.retrievers import AzureCognitiveSearchRetriever
from langchain.chains import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI, AzureChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv(dotenv_path='./azureopenai.env')

#openai.api_type = "azure"
#openai.api_base = os.getenv('AZURE_OPENAI_API_BASE')
#openai.api_key = os.getenv('AZURE_OPENAI_API_KEY')
#openai.api_version = os.getenv('AZURE_OPENAI_API_VERSION')

memory = ConversationBufferMemory(
    memory_key="chat_history", return_messages=True, output_key="answer"
)


def load_chain():
    prompt_template = """You are a helpful assistant for questions. Understand user intention and give easy/
to understand responses.
    {context}

    Question: {question}
    Answer here:"""
    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    retriever = AzureCognitiveSearchRetriever(content_key="content", top_k=10)

    llm = AzureChatOpenAI(
        openai_api_type="azure",
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        openai_api_base=os.getenv("OPENAI_API_BASE"),
        deployment_name=os.getenv("OPENAI_DEPLOYMENT_NAME"),
        model=os.getenv("OPENAI_MODEL_NAME"),
        temperature=0.7,
        openai_api_version="2023-05-15")

    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        memory=memory,
        retriever=retriever,
        combine_docs_chain_kwargs={"prompt": PROMPT},
    )

    return chain

chain = load_chain()

st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("LangChain Demo")


if 'generated' not in st.session_state:
    st.session_state['generated'] = []


if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text


user_input = get_text()

if user_input:
    output = chain.run(question=user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)



if st.session_state["generated"]:
    for i in range(len(st.session_state["generated"]) - 1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")
    #for item in output:
   # st.write("-", output)