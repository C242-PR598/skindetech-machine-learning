import os
from langchain_community.vectorstores import Chroma
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA

GOOGLE_API_KEY = "AIzaSyBO7ACt4Cg1s5_bIIo89v6QazbWOHrzeIM"
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GOOGLE_API_KEY)
persist_directory = "./db"

if not os.path.exists(persist_directory):
    raise Exception("Persist directory not found. Ensure to process and persist documents first.")

vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)
retriever = vectordb.as_retriever(search_kwargs={"k": 2})

turbo_llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash", temperature=0, google_api_key=GOOGLE_API_KEY)
qa_chain = RetrievalQA.from_chain_type(
    llm=turbo_llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

def get_answer(query: str):
    """
    Processes a query through the QA chain and returns the result and sources.

    Args:
        query (str): User's query.

    Returns:
        tuple: Result (str), Sources (list of str)
    """
    response = qa_chain(query)
    result = response['result']
    sources = [doc.metadata.get('source', 'Unknown source') for doc in response.get("source_documents", [])]
    return result, sources
