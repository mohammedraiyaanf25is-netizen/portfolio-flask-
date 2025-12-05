from flask import Flask, render_template, request, redirect, url_for, flash
from flask import send_from_directory
import os
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET', 'devsecret')

# basic routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/resume")
def resume():
    return send_from_directory('static/assets', 'resume.pdf')

@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        # choose either SEND_EMAIL via SMTP or store/send via external service
        if send_email_via_smtp(name, email, message):
            flash("Message sent — thank you!", "success")
        else:
            flash("Failed to send message. Using fallback: Save to file.", "error")
            # fallback: save to local file
            with open("messages.txt", "a", encoding="utf-8") as f:
                f.write(f"Name: {name}\nEmail: {email}\nMessage:\n{message}\n---\n")
        return redirect(url_for("contact"))
    return render_template("contact.html")

def send_email_via_smtp(name, sender_email, message_body):
    # configure these values in .env
    SMTP_HOST = os.getenv("SMTP_HOST")
    SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
    SMTP_USER = os.getenv("SMTP_USER")
    SMTP_PASS = os.getenv("SMTP_PASS")
    TO_EMAIL = os.getenv("TO_EMAIL", SMTP_USER)
    if not SMTP_HOST or not SMTP_USER or not SMTP_PASS:
        return False
    try:
        msg = EmailMessage()
        msg['Subject'] = f"Portfolio Contact from {name}"
        msg['From'] = SMTP_USER
        msg['To'] = TO_EMAIL
        msg.set_content(f"Name: {name}\nEmail: {sender_email}\n\nMessage:\n{message_body}")
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as s:
            s.starttls()
            s.login(SMTP_USER, SMTP_PASS)
            s.send_message(msg)
        return True
    except Exception as e:
        print("SMTP send failed:", e)
        return False

if __name__ == "__main__":
    # debug only for development
    app.run(host="0.0.0.0", port=5000, debug=True)