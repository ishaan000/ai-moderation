from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def moderate_content(text: str):
    response = client.moderations.create(input=text)
    result = response.results[0]

    if result.flagged:
        categories = [category for category, flagged in result.categories.dict().items() if flagged]
        return {
            "status": "flagged",
            "reason": "Content flagged for moderation",
            "categories": categories
        }

    return {
        "status": "safe",
        "reason": "Content passed moderation"
    }
