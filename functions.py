from email.message import EmailMessage
import smtplib

def generate_email(data):
    email_content = ""
    
    for article in data:
        title =  (article.get("title") or "No Title") + '\n'                 #(article["title"] + "\n")
        text = (article.get("description") or "No description") + '\n'       #article["description"] + "\n"
        url = (article.get("url" or "No url")) + '\n'                        #article["url"]  + '\n'
        author = (article.get("author") or "Unknown Author")  + '\n'

        email_content += title
        email_content += author
        email_content += text
        email_content+= url
        email_content += '\n\n'

    
    return(email_content)
        
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