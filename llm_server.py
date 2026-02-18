from fastapi import FastAPI
from pydantic import BaseModel
from llama_index.llms.ollama import Ollama

from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

app = FastAPI()

# Connect to Ollama
llm = Ollama(
    model="llama3",
    base_url="http://localhost:11434",
    temperature=0.2
)

# Request model
class Prompt(BaseModel):
    query: str

@app.post("/chat")
def chat(prompt: Prompt):
    response = llm.complete(prompt.query)
    return {"response": str(response)}
