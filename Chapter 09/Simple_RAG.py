from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForCausalLM
import faiss

# Initialize components
embedder = SentenceTransformer('all-MiniLM-L6-v2')
tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")

# Create and populate the index
chunks = ["chunk1 content", "chunk2 content", ...]
embeddings = embedder.encode(chunks)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# Retrieval and generation
def rag_query(query):
    query_embedding = embedder.encode([query])
    _, indices = index.search(query_embedding, k=3)
    context = " ".join([chunks[i] for i in indices[0]])
    prompt = f"Query: {query}\nContext: {context}\nAnswer:"
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output = model.generate(input_ids, max_length=100)
    return tokenizer.decode(output[0])
