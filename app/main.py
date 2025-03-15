from fastapi import FastAPI
from pydantic import BaseModel
from .moderation import moderate_content

app = FastAPI()

class ContentRequest(BaseModel):
    content: str

@app.post("/moderate/")
async def moderate(request: ContentRequest):
    moderation_result = moderate_content(request.content)
    return moderation_result
