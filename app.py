from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if username == "student" and password == "12345":
        return redirect("/home")

    return "Invalid username or password"

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/subject")
def subject():
    return render_template("subject.html")

@app.route("/result")
def result():
    return render_template("result.html")

@app.route("/attendance")
def attendance():
    return render_template("attendance.html")

@app.route("/assignments")
def assignments():
    return render_template("assignments.html")

@app.route("/notes")
def notes():
    return render_template("notes.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/timetable")
def timetable():
    return render_template("timetable.html")

@app.route("/performance")
def performance():
    return render_template("performance.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
