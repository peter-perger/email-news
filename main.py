from functions import generate_email, send_email
from dotenv import load_dotenv
import requests
import os

load_dotenv()
api_key=os.getenv("API_KEY")
api_url=os.getenv("API_URL").replace('API_KEY', api_key)
email_password = os.getenv("EMAIL_PASSWORD")

response = requests.get(api_url)
data = response.json()

email_content = generate_email(data["articles"][:10])
send_email(email_content, email_password)

    
