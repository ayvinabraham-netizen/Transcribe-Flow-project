\# 🎙️ TranscribeFlow



\*\*AI-powered audio transcription and summarization web application built with Flask, OpenAI Whisper, T5-small, and MySQL.\*\*



TranscribeFlow is a web-based application that allows users to upload audio files or provide recorded audio, convert speech into text using \*\*OpenAI Whisper\*\*, and generate concise summaries using the \*\*T5-small\*\* transformer model.



The application also provides downloadable transcription and summary results.



\---



\## 📌 Overview



TranscribeFlow combines web development, speech recognition, Natural Language Processing, database management, and AI model integration into a single application.



\### Core workflow



\*\*Audio → Whisper Transcription → T5 Summarization → Downloadable Result\*\*



\---



\## ✨ Features



\### 🎤 Speech-to-Text



Convert spoken audio into text using the \*\*Whisper Base\*\* model.



\### 🤖 AI Summarization



Generate a concise summary from the transcribed text using \*\*T5-small\*\*.



\### 🔐 User Authentication



The application includes:



\- User registration

\- User login

\- Session-based authentication

\- Logout



\### 📂 Audio Upload



Users can upload audio through the web interface for processing.



\### 🎙️ Recorded Audio Processing



The application supports sending recorded audio from the browser to the Flask backend.



\### 📄 Download Results



Processed results can be downloaded as:



\- TXT

\- JSON



\### 🖥️ Web Dashboard



Authenticated users can access the application's dashboard and transcription workflow.



\---



\## 🧠 How It Works



```text

&#x20;               ┌──────────────────┐

&#x20;               │      User        │

&#x20;               └────────┬─────────┘

&#x20;                        │

&#x20;                 Upload / Record

&#x20;                        │

&#x20;                        ▼

&#x20;               ┌──────────────────┐

&#x20;               │  Flask Backend   │

&#x20;               └────────┬─────────┘

&#x20;                        │

&#x20;                        ▼

&#x20;               ┌──────────────────┐

&#x20;               │  Whisper Base    │

&#x20;               │ Speech-to-Text   │

&#x20;               └────────┬─────────┘

&#x20;                        │

&#x20;                     Transcript

&#x20;                        │

&#x20;                        ▼

&#x20;               ┌──────────────────┐

&#x20;               │    T5-small      │

&#x20;               │  Summarization   │

&#x20;               └────────┬─────────┘

&#x20;                        │

&#x20;                  Summary + Text

&#x20;                        │

&#x20;                        ▼

&#x20;               ┌──────────────────┐

&#x20;               │  TXT / JSON      │

&#x20;               │    Download      │

&#x20;               └──────────────────┘

```



\---



\## 🛠️ Technology Stack



\### Backend



\- Python

\- Flask

\- PyMySQL



\### Artificial Intelligence



\- OpenAI Whisper Base

\- Hugging Face Transformers

\- T5-small



\### Frontend



\- HTML

\- CSS

\- JavaScript

\- Flask Jinja templates



\### Database



\- MySQL



\### Development Tools



\- Python virtual environment

\- Git

\- GitHub



\---



\## 📁 Project Structure



```text

Transcribe-Flow-project/

│

├── app.py

│

├── static/

│   ├── CSS

│   ├── JavaScript

│   └── frontend assets

│

├── templates/

│   ├── login.html

│   ├── register.html

│   ├── dashboard.html

│   └── upload.html

│

├── .gitignore

│

├── LICENSE

│

└── README.md

```



\---



\## ⚙️ Application Workflow



\### 1. Register



A new user creates an account through the registration page.



\### 2. Login



The user logs into the application using their credentials.



\### 3. Dashboard



After authentication, the user accesses the application dashboard.



\### 4. Upload or Record Audio



The user provides audio for processing.



\### 5. Transcription



Whisper processes the audio and converts speech into text.



```text

Audio

&#x20; ↓

Whisper Base

&#x20; ↓

Transcript

```



\### 6. Summarization



The transcript is processed using T5-small.



```text

Transcript

&#x20;   ↓

T5-small

&#x20;   ↓

Summary

```



\### 7. Download



The generated transcript and summary can be downloaded in supported formats.



\---



\## 🤖 AI Models



\### OpenAI Whisper



TranscribeFlow uses the \*\*Whisper Base\*\* model for speech recognition.



Whisper converts spoken audio into textual content.



```python

whisper\_model = whisper.load\_model("base")

```



\### T5-small



The project uses the \*\*T5-small\*\* transformer model for text summarization through the Hugging Face Transformers library.



```python

summarizer = pipeline(

&#x20;   "summarization",

&#x20;   model="t5-small"

)

```



\---



\## 💾 Database



TranscribeFlow uses \*\*MySQL\*\* for storing user information.



The Flask backend communicates with MySQL using \*\*PyMySQL\*\*.



The application currently uses a database named:



```text

flaskdb

```



The database contains user-related information required for authentication.



> For production use, database credentials should be stored in environment variables rather than directly in the source code.



\---



\## 🚀 Installation



\### 1. Clone the repository



```bash

git clone https://github.com/ayvinabraham-netizen/Transcribe-Flow-project.git

```



\### 2. Enter the project directory



```bash

cd Transcribe-Flow-project

```



\### 3. Create a virtual environment



```bash

python -m venv venv

```



\### 4. Activate the virtual environment



\#### Windows PowerShell



```powershell

venv\\Scripts\\Activate.ps1

```



\#### Windows Command Prompt



```cmd

venv\\Scripts\\activate

```



\### 5. Install the required packages



```bash

pip install flask pymysql openai-whisper transformers torch

```



Additional dependencies may be required depending on the local Python and PyTorch environment.



\---



\## 🗄️ MySQL Setup



Create the database:



```sql

CREATE DATABASE flaskdb;

```



Select the database:



```sql

USE flaskdb;

```



Create the users table:



```sql

CREATE TABLE users (

&#x20;   id INT AUTO\_INCREMENT PRIMARY KEY,

&#x20;   username VARCHAR(255) NOT NULL UNIQUE,

&#x20;   password VARCHAR(255) NOT NULL

);

```



Configure the database connection according to your local MySQL installation before running the application.



\---



\## ▶️ Running the Application



Start the Flask application:



```bash

python app.py

```



Then open the local Flask address displayed in the terminal in your browser.



\---



\## 📥 Processing Workflow



```text

Register

&#x20;  ↓

Login

&#x20;  ↓

Dashboard

&#x20;  ↓

Upload / Record Audio

&#x20;  ↓

Whisper Transcription

&#x20;  ↓

T5-small Summarization

&#x20;  ↓

View Results

&#x20;  ↓

Download TXT / JSON

```



\---



\## 📄 Output Formats



\### TXT



A text report containing the generated transcription and summary.



\### JSON



A structured report containing information such as the user, transcript, and summary.



Example:



```json

{

&#x20;   "project": "TranscribeFlow",

&#x20;   "user": "username",

&#x20;   "transcript": "...",

&#x20;   "summary": "..."

}

```



\---



\## 🔒 Security Considerations



This project was developed primarily as an educational and portfolio project.



For production deployment, the following improvements are recommended:



\- Store database credentials in environment variables

\- Hash user passwords securely

\- Use a strong Flask secret key

\- Validate uploaded files

\- Restrict file types and upload sizes

\- Add CSRF protection

\- Configure secure sessions

\- Disable Flask debug mode in production



\---



\## ⚠️ Limitations



\- AI processing depends on available system resources.

\- Whisper and T5 models can require significant memory and processing power.

\- Processing time depends on audio length and hardware.

\- The current authentication implementation is intended for learning/project purposes.

\- The Flask development server is not intended for production deployment.

\- Browser and operating-system support can affect recorded-audio functionality.



\---



\## 🔮 Future Improvements



Potential improvements include:



\- 🔐 Secure password hashing

\- ☁️ Cloud deployment

\- 📊 Transcription history

\- 👥 Improved user data isolation

\- 🌍 Multilingual transcription

\- ⚡ Background processing for long audio

\- 📱 Improved responsive UI

\- 🎙️ Better real-time transcription

\- 🧠 More advanced summarization models

\- 🔑 Environment-based configuration

\- 📈 User activity and processing history



\---



\## 🎓 Project Purpose



TranscribeFlow was developed as a practical project to explore the integration of:



\*\*Flask + MySQL + Speech Recognition + NLP + AI Models\*\*



The project provided hands-on experience in building an AI-powered web application from the user interface and backend processing to database integration and AI model usage.



\---



\## 📚 Skills Demonstrated



\- Python

\- Flask

\- MySQL

\- PyMySQL

\- HTML

\- CSS

\- JavaScript

\- Flask routing

\- Session management

\- File handling

\- Speech-to-text

\- Natural Language Processing

\- Transformer models

\- AI model integration

\- Git

\- GitHub



\---



\## 👨‍💻 Author



\*\*Ayvin Abraham\*\*



BCA Student | Python | Machine Learning | AI | Web Development



GitHub:  

https://github.com/ayvinabraham-netizen



\---



\## 📜 License



This project is licensed under the \*\*MIT License\*\*.



See the \[`LICENSE`](LICENSE) file for details.

