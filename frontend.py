import streamlit as st
from chat_bot.logic import handle_user_query # your function

st.set_page_config(page_title="Personal Care Chatbot", page_icon="💄")

st.title("💄 Personal Care Chatbot")

# Chat history
if "history" not in st.session_state:
    st.session_state.history = []

# User input
user_input = st.text_input("You:", "")

if st.button("Send") or user_input:
    if user_input:
        bot_reply = handle_user_query(user_input)  # call your chatbot_logic
        st.session_state.history.append({"user": user_input, "bot": bot_reply})

# Display chat
for chat in st.session_state.history:
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**Chatbot:** {chat['bot']}")