from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.retrievers import ContextualCompressionRetriever
import openai
from langchain.llms import OpenAI
from langchain.retrievers.document_compressors import LLMChainExtractor
import os
import sys

sys.path.append('../..')
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key  = os.environ['OPENAI_API_KEY']


# 1. loading the pdf file
loader = PyPDFLoader("./SFBU.pdf")
pages = loader.load()


#2. Splitting the loaded data
chunk_size =2000
chunk_overlap = 200
r_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size,chunk_overlap=chunk_overlap)
split = r_splitter.split_documents(pages)

# 3. VectorsStore and Embeddings
embedding = OpenAIEmbeddings()
persist_directory = 'docs/chroma/'
vectordb = Chroma.from_documents(
    documents=split,
    embedding=embedding,
    persist_directory=persist_directory
)
question = "is there an email i can ask for help"
docs = vectordb.similarity_search(question)


# 4. Retriever : Compression , only giving the relevant documents
def pretty_print_docs(docs):
    print(f"\n{'-' * 100}\n".join([f"Document {i+1}:\n\n" + d.page_content for i, d in enumerate(docs)]))
    # Wrap our vectorstore
llm = OpenAI(temperature=0)
compressor = LLMChainExtractor.from_llm(llm)
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=vectordb.as_retriever()
)

# Retrieveing the relevant data for the question
question = "What is the 100% scholarship Criteria for students applying for Masters in Computer Science?"
compressed_docs = compression_retriever.get_relevant_documents(question)
pretty_print_docs(compressed_docs)
