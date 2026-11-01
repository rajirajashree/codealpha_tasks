def get_bot_reply(message):
    message = message.lower().strip()
    if message in {"hello", "hi", "hey"}:
        return "Hi! How can I help you?"
    elif message in {"how are you", "how are you?"}:
        return "I'm fine, thanks! How are you?"
    elif message in {"what is your name", "what is your name?"}:
        return "I'm a simple Python chatbot."
    elif message in {"help", "what can you do"}:
        return "You can greet me, ask how I am, or say goodbye."
    elif message in {"bye", "goodbye", "exit", "quit"}:
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that yet. Try saying 'hello' or 'bye'."
def main():
    print("=== Basic Chatbot ===")
    print("Type 'bye' to end the conversation.")
    while True:
        user_message = input("You: ")
        reply = get_bot_reply(user_message)
        print("Bot:", reply)

        if user_message.lower().strip() in {"bye", "goodbye", "exit", "quit"}:
            break
if __name__ == "__main__":
    main()