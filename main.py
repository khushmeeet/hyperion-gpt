import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone

load_dotenv()

llm = OpenAI(client="", openai_api_key=os.getenv("OPENAI_API_KEY"))
chain = load_qa_chain(llm, chain_type="stuff")
embeddings = OpenAIEmbeddings(client="", openai_api_key=os.getenv("OPENAI_API_KEY"))

query = "What is Benares?"
pinecone.init(api_key=os.getenv("PINECOE_API_KEY"), environment="us-west4-gcp")
index = Pinecone.from_existing_index(index_name="hyperion-index", embedding=embeddings)
docs = index.similarity_search(query, namespace="hyperion")
ans = chain.run(input_documents=docs, question=query)
print(ans)
