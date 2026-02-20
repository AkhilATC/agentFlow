
# Connect LlamaIndex and Ollama
from llama_index.llms.ollama import Ollama
from llama_index.core import Settings

Settings.llm = Ollama(model="llama3")
