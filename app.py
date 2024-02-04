import streamlit as st
from utils import get_vectorstore_from_url,get_response
from langchain_core.messages import AIMessage, HumanMessage
import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain





st.set_page_config(page_title="Chat with websites", page_icon="🤖")
st.title('Chat with RAG using URL Content')
with st.sidebar:
# Input for URL
    url = st.text_input('Enter URL', '')

if url is None or url == "":
    st.info("Please enter a website URL")

else:
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            AIMessage(content="Hello, I am a bot. How can I help you?"),
        ]
    if "vectorstore" not in st.session_state:
        st.session_state.vectorstore = get_vectorstore_from_url(url)
    
        # Input for user query
    user_query = st.chat_input('Enter your query')
    if user_query is not None and user_query !="":
        response=get_response(user_query)
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        st.session_state.chat_history.append(AIMessage(content=response))     

    # conversation
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.write(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("Human"):
                st.write(message.content)

