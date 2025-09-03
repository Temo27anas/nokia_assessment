from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

import os

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
GRADIENT_TRSH = 50
TEXT_PATH_EXAMPLE = "file.txt"

def chuncker(TEXT_PATH_EXAMPLE):
    with open(TEXT_PATH_EXAMPLE) as f:
        try:
            file_content = f.read()
        except UnicodeDecodeError:
            print("Error During Decoding. Check Characters")
            exit()

    text_splitter = SemanticChunker(OpenAIEmbeddings(), breakpoint_threshold_type="gradient", breakpoint_threshold_amount = GRADIENT_TRSH)

    docs = text_splitter.create_documents([file_content])

def prompter(docs):
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    chunk_embeddings = model.encode(docs)
    print(chunk_embeddings.shape)  


