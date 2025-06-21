from langchain_ollama.chat_models import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

llm = ChatOllama(model="llama3.1", temperature=0.7)

async def get_llm_response(message: str) -> str:
    response = await llm.ainvoke([
        SystemMessage(content="You are a helpful and challenging AI interview coach. Don't give direct answers. Instead, guide the user to think critically."),
        HumanMessage(content=message)
    ])
    if isinstance(response.content, str):
        return response.content
    else:
        return str(response.content)