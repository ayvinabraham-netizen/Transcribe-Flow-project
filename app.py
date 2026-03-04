import os
import pymysql
import whisper
from flask import Flask, render_template, request, redirect, url_for, session
from transformers import pipeline
from flask import send_file
from io import BytesIO
import json
app = Flask(__name__)
app.secret_key = "secretkey"

# ---------------- Upload Folder Setup ----------------
upload_folder = "uploads"
os.makedirs(upload_folder, exist_ok=True)
app.config["UPLOAD_FOLDER"] = upload_folder

# ---------------- Load Models Once ----------------
print("Loading Whisper model...")
whisper_model = whisper.load_model("base")
print("Whisper model loaded!")

print("Loading Summarization model...")
summarizer = pipeline("summarization", model="t5-small")
print("Summarization model loaded!")

# ---------------- Transcription Function ----------------
def transcribe_audio(audio_file):
    result = whisper_model.transcribe(audio_file)
    return result['text']

# ---------------- Summarization Function ----------------
def summarize_text(text):
    input_text = "summarize: " + text   # Important for T5
    summary = summarizer(
        input_text,
        max_length=120,
        min_length=40,
        do_sample=False
    )
    return summary[0]['summary_text']


# ---------------- Login Page ----------------
@app.route("/")
def home():
    return render_template("login.html")


# ---------------- Login ----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        try:
            conn = pymysql.connect(
                host="127.0.0.1",
                user="root",
                password="Ayvin@password",
                database="flaskdb",
                port=3306
            )
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM users WHERE username=%s AND password=%s",
                (username, password)
            )
            user = cursor.fetchone()
            cursor.close()
            conn.close()

            if user:
                session["user"] = username
                return redirect(url_for("dashboard"))
            else:
                return "Invalid Credentials"

        except Exception as e:
            return str(e)

    return render_template("login.html")


# ---------------- Register ----------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        try:
            conn = pymysql.connect(
                host="127.0.0.1",
                user="root",
                password="Ayvin@password",
                database="flaskdb",
                port=3306
            )
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
            existing_user = cursor.fetchone()

            if existing_user:
                return "Username already exists!"

            cursor.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                (username, password)
            )
            conn.commit()
            cursor.close()
            conn.close()

            return redirect(url_for("home"))

        except Exception as e:
            return str(e)

    return render_template("register.html")


# ---------------- Dashboard ----------------
@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return render_template("dashboard.html", user=session["user"])
    return redirect(url_for("home"))


# ---------------- Upload + Transcribe + Summarize ----------------
@app.route("/upload", methods=["GET", "POST"])
def upload():
    if "user" not in session:
        return redirect(url_for("home"))

    if request.method == "POST":
        if "file" not in request.files:
            return "No file part"

        file = request.files["file"]

        if file.filename == "":
            return "No selected file"

        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            print("Transcribing...")
            transcript = transcribe_audio(filepath)

            print("Summarizing...")
            summary = summarize_text(transcript)

            # Save in session for download
            session["transcript"] = transcript
            session["summary"] = summary

            return render_template(
                "upload.html",
                transcript=transcript,
                summary=summary
            )

    return render_template("upload.html")

@app.route("/download")
def download():
    if "user" not in session:
        return redirect(url_for("home"))

    transcript = session.get("transcript")
    summary = session.get("summary")

    if not transcript or not summary:
        return redirect(url_for("upload"))

    content = f"""
TRANSCRIBEFLOW REPORT
======================

--- TRANSCRIPT ---
{transcript}

--- AI SUMMARY ---
{summary}
"""

    buffer = BytesIO()
    buffer.write(content.encode("utf-8"))
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="transcription_report.txt",
        mimetype="text/plain"
    )
@app.route("/download-json")
def download_json():
    if "user" not in session:
        return redirect(url_for("home"))

    transcript = session.get("transcript")
    summary = session.get("summary")

    if not transcript or not summary:
        return redirect(url_for("upload"))

    data = {
        "project": "TranscribeFlow",
        "user": session.get("user"),
        "transcript": transcript,
        "summary": summary
    }

    json_data = json.dumps(data, indent=4)

    buffer = BytesIO()
    buffer.write(json_data.encode("utf-8"))
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="transcription_report.json",
        mimetype="application/json"
    )
@app.route("/record", methods=["POST"])
def record():
    if "user" not in session:
        return {"error": "Unauthorized"}, 401

    audio = request.files.get("audio")

    if not audio:
        return {"error": "No audio received"}, 400

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], "live_recording.wav")
    audio.save(filepath)

    # Transcribe
    transcript = transcribe_audio(filepath)

    # Summarize
    summary = summarize_text(transcript)

    # Store for download
    session["transcript"] = transcript
    session["summary"] = summary

    return {
        "transcript": transcript,
        "summary": summary
    }
# ---------------- Logout ----------------
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)