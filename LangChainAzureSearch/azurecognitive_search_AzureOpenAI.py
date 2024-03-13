import os
import openai
from os.path import join, dirname
from langchain_openai import OpenAIEmbeddings

from langchain.vectorstores.azuresearch import AzureSearch
from langchain_community.document_loaders import AzureBlobStorageContainerLoader
from langchain.text_splitter import CharacterTextSplitter
from dotenv import load_dotenv

#dotenv_path = join(dirname(__file__), '.env')
#load_dotenv(dotenv_path)
load_dotenv()

openai.api_type = "azure"
openai.api_base = os.getenv('AZURE_OPENAI_API_BASE')
openai.api_key = os.getenv('AZURE_OPENAI_API_KEY')
openai.api_version = os.getenv('AZURE_OPENAI_API_VERSION')

model: str = os.environ.get('AZURE_OPENAI_EMBEDDING_MODEL_NAME')
#"text-embedding-3-large"

vector_store_address: str = f"https://{os.environ.get('AZURE_COGNITIVE_SEARCH_SERVICE_NAME')}.search.windows.net"
print(vector_store_address)


#embeddings: OpenAIEmbeddings = OpenAIEmbeddings(deployment=model, chunk_size=1)


embeddings = OpenAIEmbeddings(
    openai_api_type="azure",
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_base=os.getenv("OPENAI_API_BASE"),
    deployment=os.getenv("OPENAI_DEPLOYMENT_NAME"),
    model=os.getenv("OPENAI_MODEL_NAME"),
    chunk_size=1)

index_name: str = "langchain-vector-demo"
vector_store: AzureSearch = AzureSearch(
    azure_search_endpoint=vector_store_address,
    azure_search_key=os.environ.get("AZURE_COGNITIVE_SEARCH_API_KEY"),
    index_name=index_name,
    embedding_function=embeddings.embed_query,
)

loader = AzureBlobStorageContainerLoader(
    conn_str=os.environ.get("AZURE_CONN_STRING"),
    container=os.environ.get("CONTAINER_NAME"),
)
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1500, chunk_overlap=20)
docs = text_splitter.split_documents(documents)
vector_store.add_documents(documents=docs)

print("Data loaded into vector store successfully")
