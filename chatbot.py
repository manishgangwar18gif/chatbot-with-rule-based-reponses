import re

def chatbot():
    print("Bot: Hello! I am your chatbot.")
    print("Bot: Type 'bye' to exit.")

    while True:
        user_input = input("You: ").strip().lower()

        # Exit rule
        if user_input in ["bye", "exit", "quit"]:
            print("Bot: Goodbye! Have a nice day.")
            break

        # Greeting rules
        elif re.search(r"\b(hi|hello|hey)\b", user_input):
            print("Bot: Hello! How can I help you?")

        # Name rule
        elif "your name" in user_input or "who are you" in user_input:
            print("Bot: I am a rule-based chatbot.")

        # Feeling rule
        elif "how are you" in user_input:
            print("Bot: I am fine! Thanks for asking.")

        # Help rule
        elif "help" in user_input:
            print("Bot: Sure! Tell me what you need help with.")

        # Thanks rule
        elif "thank" in user_input:
            print("Bot: You are welcome!")

        # Default response
        else:
            print("Bot: Sorry, I don't understand that yet.")


if __name__ == "__main__":
    chatbot()