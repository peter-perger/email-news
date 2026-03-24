from email.message import EmailMessage
import smtplib

def generate_articles(data):
    article_content = ""
    
    for article in data['articles']:
        title =  (article.get("title") or "No title for this article")                  
        text = (article.get("description") or "No description for this article") + '\n'       
        url = (article.get("url") or "No url for this article") + '\n'                        
        author = (article.get("author") or "No auhtor for this article") + '\n'

        article_content += title
        article_content += author
        article_content += text
        article_content+= url
        article_content += '\n\n'

    return(article_content)

def get_title_url(data):
    text = ""
    
    for article in data['articles']:
        title =  (article.get("title") or "No title for this article")
        url = (article.get("url") or "No url for this article") + '\n' 

        text += title + "\n"
        text += url + '\n'

    return text
        
def send_email(email_content, password):
    sender_email = "pergerpeti2@gmail.com"
    reciever_email = "pergerpeti2@gmail.com"

    msg = EmailMessage()
    msg["Subject"] = "Todays News"
    msg["From"] = sender_email
    msg["To"] = reciever_email
    msg.set_content(email_content)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, password)
            smtp.send_message(msg)
        print("Email sent succesfully ✅")
    except Exception as e:
        print(f"Error: {e}")
