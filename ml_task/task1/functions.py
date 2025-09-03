from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sklearn.metrics.pairwise import cosine_similarity
from openai import OpenAI
import os

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
GRADIENT_TRSH = 50
TEXT_PATH_EXAMPLE = "file.txt"

def chuncker_semantic(TEXT_PATH_EXAMPLE):
    with open(TEXT_PATH_EXAMPLE) as f:
        try:
            file_content = f.read()
        except UnicodeDecodeError:
            print("Error During Decoding. Check Characters")
            exit()

    text_splitter = SemanticChunker(OpenAIEmbeddings(), breakpoint_threshold_type="gradient", breakpoint_threshold_amount = GRADIENT_TRSH)

    docs = text_splitter.create_documents([file_content])
    return docs

def chucker_recusrsive(file_content):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 200,        # target chunk size in characters (or tokens)
        chunk_overlap = 50,      # overlap to maintain context between chunks
        separators = ["\n\n", "\n", " ", ""]  
        # The splitter will try to split by double newline (paragraph), then newline, then space, then as last resort character.
    )
    chunks = text_splitter.split_text(file_content)
    print(f"Created {len(chunks)} chunks with recursive splitting.")
    print(chunks[0][:100]) 
    return chunks

def embedder(docs):
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    chunk_embeddings = model.encode(docs)
    print(chunk_embeddings.shape) 
    return chunk_embeddings

# Get top chunks for the query
def get_top_chunks(query, chunk_embeddings, docs, top_n=5):
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, chunk_embeddings)
    top_indices = similarities[0].argsort()[-top_n:][::-1]
    return [(docs[i], similarities[0][i]) for i in top_indices]

# Prompting
def prompt_to_llm(master_prompt):
    # Open AI API call
    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": master_prompt
            }
        ]
    )
    return response.choices[0].message.content

def parse_response(llm_response):
    if "NOT FOUND" in llm_response:
        return "NOT FOUND"
    
    try:
        answer_part = llm_response.split("Answer:")[1].split("| Citations:")[0].strip()
        citations_part = llm_response.split("| Citations:")[1].strip()
        citations = [cit.strip() for cit in citations_part.split(";") if cit.strip()]
        return {
            "answer": answer_part,
            "citations": citations
        }
    except IndexError:
        print("Error parsing LLM response. Check the response format.")
        return None
    
def pipeline(file_content, query):
    chuncks = chucker_recusrsive(file_content)
    embeddings = embedder(chuncks)
    top_chunks = get_top_chunks(query, embeddings, chuncks)

    master_prompt = "Answer only using the provided context snippets." \
                + "You will be provided 5 chunks of text. Your task is to answer the question based on these chunks: \n" \
                + "\n\n".join([f"Chunk {i+1}: {chunk}" for i, (chunk, _) in enumerate(top_chunks)]) \
                + "QUESTION: " + query + "\n\n" \
                + "* If you can answer, provide citations (only relevant ones) as the following:" + "\n" \
                + "Answer: <YOUR ANSWER> | Citations: <chunk_id> <preview from chunk>; <chunk_id> <preview from chunk> ... \n\n" \
                + "* If the answer isn't supported by the context, reply: <NOT FOUND> - Be concise."
    
    llm_response = prompt_to_llm(master_prompt)
    results = parse_response(llm_response)
    return results

    