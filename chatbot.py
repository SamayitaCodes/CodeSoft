# chatbot.py

def respond_to_user(input_text):
    # Define some simple rules for responses
    rules = {
        "hi": "Hello! How can I help you today?",
        "hello": "Hi there! What can I do for you?",
        "how are you": "I'm just a bot, but I'm here to help you!",
        "bye": "Goodbye! Have a great day!",
        "default": "I'm sorry, I don't understand that."
    }

    # Normalize the input text to lower case
    input_text = input_text.lower()

    # Respond based on the rules
    for key in rules:
        if key in input_text:
            return rules[key]
    return rules["default"]

def main():
    print("Welcome to the rule-based chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Bot: Goodbye! Have a great day!")
            break
        response = respond_to_user(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()

