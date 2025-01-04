from google import genai
from config import Settings

settings = Settings()

class Search:
  def web_search(self, query: str):
    client = genai.Client(api_key=settings.GEMINI_API_KEY)
    response = client.models.generate_content(model='gemini-2.0-flash-exp', contents=[query])
    print(response.text)
   