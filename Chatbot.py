# -----------------------------------
# Basic Rule-Based Chatbot in Python
# -----------------------------------

# Function to display welcome message
def show_welcome():
    print("===================================")
    print(" Welcome to Simple Chatbot")
    print("Type 'bye' to exit the chat")
    print("===================================")


# Function to get bot response
def chatbot_response(user_input):
    user_input = user_input.lower()  # convert input to lowercase

    if user_input == "hello" or user_input == "hi":
        return "Hi! Nice to meet you "

    elif user_input == "how are you":
        return "I'm fine, thanks for asking!"

    elif user_input == "what is your name":
        return "I am a simple rule-based chatbot."
        
    elif user_input == "help":
        return "You can say: hello, how are you, what is your name, or bye."

    elif user_input == "bye":
        return "Goodbye! Have a great day "

    else:
        return "Sorry, I don't understand that."


# Main function
def start_chatbot():
    show_welcome()

    while True:
        user_input = input("You: ")

        response = chatbot_response(user_input)
        print("Bot:", response)

        if user_input.lower() == "bye":
            break


# Run the chatbot
start_chatbot()
