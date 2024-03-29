import argparse
import io
import sys
import time
from langchain_community.llms import Ollama
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain.prompts import HumanMessagePromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import UnstructuredMarkdownLoader
import threading


def show_loading():
    chars = "/—\\|"
    i = 0
    while not done:
        sys.stdout.write("\r" + "Loading... " + chars[i % len(chars)])
        sys.stdout.flush()
        i += 1
        time.sleep(0.1)


# Start the loading animation in a separate thread
done = False
loading_thread = threading.Thread(target=show_loading)
loading_thread.start()
# Create ArgumentParser object
parser = argparse.ArgumentParser(description="You own command line RAG.")

# Add arguments
parser.add_argument(
    "-t", "--type", type=str, help="File/Content type. One of `md`, `pdf`, or `web`."
)
parser.add_argument("-f", "--filename", type=str, help="File name / Web url")
parser.add_argument("-q", "--question", type=str, help="The question to ask the model.")

# Parse the arguments
args = parser.parse_args()

# Access the arguments
filename = args.filename
question = args.question
content_type = args.type

if filename is None:
    filename = input("Enter filename: ")

if question is None:
    question = input("Enter question: ")

if content_type is None:
    content_type = input("Enter content type: ")

llm = Ollama(model="mistral:7b-instruct", temperature=0.8)

if content_type == "md":
    loader = UnstructuredMarkdownLoader(filename)
    docs = loader.load()
elif content_type == "pdf":
    loader = PyPDFLoader(filename)
    docs = loader.load_and_split()
elif content_type == "web":
    loader = WebBaseLoader(filename)
    docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)

embedding = GPT4AllEmbeddings()
vectorstore = Chroma.from_documents(documents=splits, embedding=embedding)

# Retrieve and generate using the relevant snippets of the blog.
retriever = vectorstore.as_retriever()
prompt = ChatPromptTemplate(
    input_variables=["context", "question"],
    messages=[
        HumanMessagePromptTemplate(
            prompt=PromptTemplate(
                input_variables=["context", "question"],
                template="You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Keep the answer concise.\nQuestion: {question} \nContext: {context} \nAnswer:",
            )
        )
    ],
)


def format_docs(docs):
    formatted_doc = "\n\n".join(doc.page_content for doc in docs)
    return formatted_doc


rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)
done = True
loading_thread.join()
answer = rag_chain.invoke(question)
print("\r")
print("=================== Answer ===================")
print(answer.strip())
