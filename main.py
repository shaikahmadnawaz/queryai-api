from fastapi import FastAPI
from models.chat import Chat
from services.search import Search

app = FastAPI()

search = Search()

# Chat
@app.post("/api/v1/chat")
async def chat(body: Chat):
    search.web_search(body.query)
    # 2. Sort the sources by relevance
    # 3. Generate the response using LLM (GPT-4o)
    return {"query": body.query}