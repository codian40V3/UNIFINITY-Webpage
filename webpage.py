import os
from flask import Flask, render_template, send_from_directory, request
from flask_mail import Mail, Message
from config import sender_mail_username, sender_mail_password, recipient_mail_username


app = Flask(__name__)

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = sender_mail_username
app.config["MAIL_PASSWORD"] = sender_mail_password


mail = Mail(app)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")

        msg = Message(sender=sender_mail_username, recipients=recipient_mail_username,
                      subject="UNIFINITY Contact Form submission", body=f"Email: {email}\nSubject: {subject}"
                                                                        f"\n\n{message}")
        mail.send(msg)
    return render_template("contact.html")


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'Favicon Transparent.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == "__main__":
    app.run()
