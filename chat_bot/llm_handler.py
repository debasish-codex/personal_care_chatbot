# llm_handler.py

import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv


# Load .env file
load_dotenv()

def get_llm_response(user_input):

    # 🔹 Step 1: Get API key and model from .env
    api_key = os.getenv("GROQ_API_KEY")
    model_name = os.getenv("GROQ_MODEL")

    # 🔹 Step 2: Create LLM using LangChain
    llm = ChatGroq(
        groq_api_key=api_key,
        model_name=model_name
    )

    # 🔹 Step 3: Prepare message
    prompt = "Answer this question about personal care in simple terms: " + user_input

    message = HumanMessage(content=prompt)

    # 🔹 Step 4: Call LLM
    try:
        response = llm.invoke([message])

        reply = response.content

    except Exception as e:
        reply = "Sorry, I am unable to answer right now."

    # 🔹 Step 5: Return response
    return reply