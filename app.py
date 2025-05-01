from flask import Flask, request, jsonify, render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

EMAIL_USER = 'infovmars.01@gmail.com'
EMAIL_PASS = 'ohoo fvux bakh mgsm'  # Your Gmail app password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    subject = data.get('subject')
    message = data.get('message')

    # Create email message
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = 'info@vmarsbio.com'
    msg['Subject'] = f"New Contact Form Submission: {subject}"

    # Create email body
    body = f"""
    New message from the website contact form:
    
    Name: {name}
    Email: {email}
    Subject: {subject}
    
    Message:
    {message}
    """
    
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to Gmail SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        
        # Send email
        server.sendmail(EMAIL_USER, 'info@vmarsbio.com', msg.as_string())
        server.quit()
        
        return jsonify({"message": "Email sent successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
