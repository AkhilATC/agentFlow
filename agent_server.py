from fastapi import FastAPI
from pydantic import BaseModel
from llama_index.llms import Ollama
from llama_index.core.agent import ReActAgent

app = FastAPI()

llm = Ollama(model="llama3")

agent = ReActAgent.from_tools(
    tools=[],  # later we add Mongo, HTTP, etc.
    llm=llm,
    verbose=True
)

class Prompt(BaseModel):
    query: str

@app.post("/agent")
def run_agent(prompt: Prompt):
    response = agent.chat(prompt.query)
    return {"response": str(response)}
