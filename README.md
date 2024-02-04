# Chat with Websites

A Streamlit application that allows users to interact with website content through a conversational AI interface. This app leverages the LangChain library to retrieve information from specified websites, chunk the content, create a vector store for efficient information retrieval, and generate responses to user queries based on the website's content.

## Features

- **Website Content Interaction:** Users can chat with the application to get information from a specified website URL.
- **Conversational Context Understanding:** The application maintains a conversation history to provide context-aware responses.
- **Dynamic Information Retrieval:** Utilizes LangChain for dynamic content retrieval and processing from websites.

## Installation

To run this application, you need Python 3.6 or later. Clone this repository and install the required dependencies.

```bash
git clone <repository-url>
cd <repository-directory>
pip install streamlit langchain langchain-openai beautifulsoup4 python-dotenv chromadb
streamlit run app.py
