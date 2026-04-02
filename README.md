# Personal Care Chatbot

A personal care product chatbot powered by an LLM that can:

- Answer general queries about products (e.g., benefits, usage).  
- Provide product suggestions based on price, brand, or category.  
- Redirect users to support for returns, offers, or refunds.  
- Store all conversations in a PostgreSQL database.

---

## 🗄 Database

PostgreSQL is used to store user queries and chatbot responses.  
Table `chat_logs` stores:

| Column         | Description           |
|----------------|----------------------|
| id             | Primary key          |
| user_message   | User input           |
| bot_response   | Chatbot reply        |

Access data via pgAdmin or SQL queries.

<img width="1552" height="397" alt="Database Screenshot" src="https://github.com/user-attachments/assets/e0dd7e65-9dc5-4d15-8adc-80225bd7101a" />

---

## 🤖 LLM (Groq + LangChain)

- Uses **Groq LLM** to answer general queries.  
- **LangChain** wraps the LLM calls for easier integration.

## ⚙️ Setup Instructions
```bash

1️⃣ Clone the repository
git clone <your_repo_url>
cd personal_care_chatbot
2️⃣ Create a virtual environment
python -m venv venv
3️⃣ Activate virtual environment

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate
4️⃣ Install dependencies
pip install -r requirements.txt
5️⃣ Setup .env file
LLM_MODEL=groq-llm
LLM_API_KEY=your_api_key_here
DB_NAME=chatbot_db
DB_USER=postgres
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
6️⃣ Run PostgreSQL server
Ensure PostgreSQL is installed and running.
Create a database (e.g., chatbot_db).
🚀 Run the Chatbot

CLI version:

python app.py

Frontend (optional Streamlit version):

streamlit run frontend.py
⚡ Features
Product search with filters (price, brand)
LLM-powered general queries (benefits, usage)
Redirect to support for returns, refunds, and offers
Store conversations in PostgreSQL
🖋 Developed By

Debasish Pradhan


✅ Key points:
- Use **triple backticks ```** for code blocks → ensures commands are line by line  
- Use **two spaces at end of line** (or `-` bullets) to create line breaks in Markdown  
- Use `---` to separate sections  

---

If you want, I can **combine this Setup section with your full chatbot README including database, LLM, and screenshots** in a **single professional README** ready for GitHub.  

Do you want me to do that next?
