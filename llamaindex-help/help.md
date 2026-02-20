## LlamaIndex

```text
It helps you:
1. Load PDFs, docs, DBs, APIs
2. Convert them into embeddings
3. Store in vector DB
4. Query using GPT / Ollama / Claude
5. Build chatbots, agents, search engines
```

# EMBEDDINGS

> light weight Settings.embed_model = HuggingFaceEmbedding(model_name="nomic-ai/nomic-embed-text-v1")


## OLLAMA PULLS
✅ Step 1: Check Ollama Inside Docker
docker exec -it <container_id> ollama list
✅ Step 2: Pull llama3 INSIDE Docker
docker exec -it 232e7f5c5a54 ollama pull llama3
or
docker exec -it 232e7f5c5a54 ollama pull llama3:8b

