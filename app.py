# app.py

from chat_bot.logic import handle_user_query
from database.db import create_table

def main():

    # 🔹 Step 1: Create table (if not exists)
    create_table()

    print("Welcome to Personal Care Chatbot!")
    print("Type 'exit' to quit.\n")

    # 🔹 Step 2: Start loop
    while True:

        # Take user input
        user_input = input("You: ")

        # Check exit condition
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        # 🔹 Step 3: Get response
        bot_reply = handle_user_query(user_input)

        # 🔹 Step 4: Print response
        print("Chatbot:", bot_reply)


# 🔹 Step 5: Run program
if __name__ == "__main__":
    main()