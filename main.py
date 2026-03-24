from langchain.chat_models import init_chat_model 
from functions import generate_articles, get_title_url, send_email
from dotenv import load_dotenv
import requests
import os

load_dotenv()
api_key=os.getenv("API_KEY")
api_url=os.getenv("API_URL").replace('API_KEY', api_key)
email_password = os.getenv("EMAIL_PASSWORD")
gemini_api_key = os.getenv("GEMINI_API_KEY")

model = init_chat_model(
    model="gemini-3-flash-preview", 
    model_provider="google-genai", 
    api_key = gemini_api_key
)

response = requests.get(api_url)
data = response.json()

articles = generate_articles(data)


prompt = f"""
Act as a news summarizer. Summarize the following articles in a single short paragraph.
In a second paragraph, summarize which sports and teams are undergoing the most significant changes.

Here are the artciles: {articles}
"""

response = model.invoke(prompt)
response_string = response.content[0]["text"]

title_url_string = get_title_url(data)

email_content = f"{response_string} '\n \n {title_url_string}"


send_email(email_content, email_password)