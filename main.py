# Simple Rule-Based Chatbot

def chatbot():
    print("Hello! Type something to start a chat. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello":
            print("Chatbot: hi!")

        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")

        elif user_input == "bye":
            print("goodbye!")
            break

        else:
            print("Sorry, I don't understand that.")

# Run the chatbot function
chatbot()
