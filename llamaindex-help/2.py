"""
Documents → Chunking → Embeddings → Vector Index → Query → LLM
DOC: OOH1-6MD FILES
"""
# LOAD CORPUS IN LLAMA 🫶
from llama_index.core import SimpleDirectoryReader,VectorStoreIndex
from llama_index.llms.ollama import Ollama
from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding



# OLLAMA CONNECTION
Settings.llm = Ollama(model="llama3")
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
# load corpus in llama
print("[TAG] LOAD CORPUS IN LLAMA 💾")
"""
💾 8️⃣ Persist Index (Important for Production)

Without this → index rebuilds every run.
"""
documents  = SimpleDirectoryReader("corpus").load_data()
# print(documents)
print("[TAG] CREATE INDEX IN LLAMA 🗂️")
# USE OLLAMA OR ANY OTHER EMMBEDINGS
# Build index
index = VectorStoreIndex.from_documents(documents)
print("[TAG] BUILD QUERY ENGINE IN LLAMA 🗂️")
# Query engine build
query_engine = index.as_query_engine()
if __name__ == '__main__':
    while True:
        q = input("ASK ME [🥷] ABOUT OOH IN KERALA : ")
        if q.lower() == "exit":
            break
        response = query_engine.query(q)
        print("🤖", response)
