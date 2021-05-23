from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy

# from sqlalchemy.sql import func
from werkzeug.utils import secure_filename

# from send_email import send_email

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# For local development, run `from app import db` and `db.create_all()`
# in a terminal to create all the tables that have associated models
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://postgres:changeme@localhost:5432/height_collector"
# # Heroku
# app.config['SQLALCHEMY_DATABASE_URI']='postgres://ejwuclujctbntz:2ZvGfcHUFzmasNYi-TwQH6lMgf@ec2-50-17-206-164.compute-1.amazonaws.com:5432/d425fslp62inet?sslmode=require'
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    height_ = db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success", methods=["POST"])
def success():
    global file
    if request.method == "POST":
        # # Send data to database
        # email = request.form['email_name']
        # height = request.form['height_name']
        # if db.session.query(Data).filter(Data.email_==email).count() == 0:
        #   data = Data(email, height)
        #   db.session.add(data)
        #   db.session.commit()
        #   Get the numeric average of all heights in db with func.avg
        #   average_height = db.session.query(func.avg(Data.height_)).scalar()
        #   average_height = round(average_height, 1)
        #   count=db.session.query(Data.height_).count()
        #   send_email(email, height, average_height, count)
        #   return render_template("success.html")

        # return render_template("index.html", text="email already exists")

        file = request.files["file"]
        # Sanitize filename for file name entered by the user with secure_filename
        file_name = secure_filename("uploaded" + file.filename)
        file.save(file_name)
        with open(file_name, "a") as f:
            f.write("This was added later on!")
        print(file)
        print(type(file))
        return render_template("index.html", btn="download.html")


@app.route("/download")
def download():
    """
    pass
    """
    return send_file(
        "uploaded" + file.filename,
        attachment_filename="yourfile.csv",
        as_attachment=True,
    )


if __name__ == "__main__":
    app.debug = True
    app.run()
