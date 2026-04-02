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

  `.env` file stores:

```env
LLM_MODEL=groq-llm
LLM_API_KEY=your_api_key_here


⚙️ Setup Instructions
Clone the repository:

git clone <your_repo_url>
cd personal_care_chatbot

Create a virtual environment:
python -m venv venv

Activate virtual environment:
Windows:
venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Setup .env file:
LLM_MODEL=groq-llm
LLM_API_KEY=your_api_key_here
DB_NAME=chatbot_db
DB_USER=postgres
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

Run PostgreSQL server and create a database (e.g., chatbot_db).

.
🚀 Run the Chatbot
CLI version:

python app.py

Frontend (optional Streamlit version):
streamlit run frontend.py
<img width="1565" height="877" alt="Chatbot Screenshot" src="https://github.com/user-attachments/assets/c824b284-66c9-45ae-a5bc-a4c5a95a7c06" />

⚡ Features
Product search with filters (price, brand).
LLM powered general queries (benefits, usage).
Redirect to support for returns, refunds, and offers.
Store conversations in PostgreSQL.

🖋 Developed By

Debasish Pradhan
