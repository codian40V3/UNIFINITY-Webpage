import os
from flask import Flask, render_template, send_from_directory, request
from flask_mail import Mail, Message
from dotenv import dotenv_values

config = dotenv_values(".env")
config_list = [config]

app = Flask(__name__)

app.config["MAIL_SERVER"] = "smtppro.zoho.eu"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USERNAME"] = config["unifinity_sender_username"]
app.config["MAIL_PASSWORD"] = config["unifinity_sender_password"]

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

        msg = Message(sender=config.get("unifinity_sender_username"),
                      recipients=[config.get("unifinity_recipient_username")],
                      subject="UNIFINITY Contact Form submission",
                      body=f"Email: {email}\nSubject: {subject}\n\n{message}")
        mail.send(msg)
    return render_template("contact.html")


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'Favicon Transparent.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == "__main__":
    app.run()
