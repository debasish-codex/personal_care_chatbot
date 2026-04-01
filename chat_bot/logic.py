

from chat_bot.intent_detector import detect_intent
from chat_bot.product_search import search_products
from chat_bot.llm_handler import get_llm_response
from database.db import save_chat

def handle_user_query(user_input):

    # 🔹 Step 1: Detect intent
    intent = detect_intent(user_input)

    # 🔹 Step 2: Initialize reply
    bot_reply = ""

    # 🔹 Step 3: Handle different intents

    # ✅ Product Query
    if intent == "product":

        products = search_products(user_input)

        if len(products) == 0:
            bot_reply = "No products found matching your query."
        else:
            response_lines = []

            for product in products:
                line = ""
                line = line + "Brand: " + product["Brand"] + ", "
                line = line + "Product: " + product["Product Name"] + ", "
                line = line + "Price: " + product["Current Price"]

                response_lines.append(line)

            bot_reply = "\n".join(response_lines)

    # ✅ General Query
    elif intent == "general":

        bot_reply = get_llm_response(user_input)

    # ✅ Support Query
    elif intent == "support":

        bot_reply = "Please contact support: +91 99xxxxx235"

    # ✅ Unknown Query
    else:

        bot_reply = "Sorry, I didn’t understand. Please ask about products or personal care."

    # 🔹 Step 4: Save chat in database
    save_chat(user_input, bot_reply)

    # 🔹 Step 5: Return response
    return bot_reply