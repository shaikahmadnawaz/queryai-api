from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch
from config import Settings

settings = Settings()

class Search:
  def web_search(self, query: str):
    client = genai.Client(api_key=settings.GEMINI_API_KEY)
    model_id = "gemini-2.0-flash-exp"
    google_search_tool = Tool(
        google_search=GoogleSearch()
    )

    response = client.models.generate_content(
        model=model_id,
        contents=[query],
        config=GenerateContentConfig(
            tools=[google_search_tool],
            response_modalities=["TEXT"],
        )
    )

    for each in response.candidates[0].content.parts:
      print(each.text)