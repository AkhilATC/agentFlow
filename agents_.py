small_talk_agent = ReActAgent.from_tools(
    tools=[],
    llm=llm,
    system_prompt="You are a friendly conversational assistant."
)



from llama_index.core.tools import FunctionTool

def mongo_write_tool(data: dict):
    print("Writing to Mongo:", data)
    return {"status":"ok"}

mongo_tool = FunctionTool.from_defaults(fn=mongo_write_tool)

db_agent = ReActAgent.from_tools(
    tools=[mongo_tool],
    llm=llm,
    system_prompt="Handle database operations."
)
