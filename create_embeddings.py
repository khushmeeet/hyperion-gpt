import os
from dotenv import load_dotenv
from langchain.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma, Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone

load_dotenv()

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)


def split_documents():
    for i in os.listdir("./data"):
        loader = UnstructuredFileLoader("./data/" + i, mode="elements")
        doc = loader.load()
        yield splitter.split_documents(doc)


if __name__ == "__main__":
    embeddings = OpenAIEmbeddings(client="", openai_api_key=os.getenv("OPENAI_API_KEY"))
    pinecone.init(api_key=os.getenv("PINECOE_API_KEY"), environment="us-west4-gcp")
    for docs in split_documents():
        pinecone_embeddings = Pinecone.from_texts(
            [d.page_content for d in docs],
            embeddings,
            index_name="hyperion-index",
            namespace="hyperion",
        )
