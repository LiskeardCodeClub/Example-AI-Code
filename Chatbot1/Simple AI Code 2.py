 #Simple dictionary definining keywords that the AI will reply to and responses it will give. Quite limitted, see Dictionary ChatBot for ways around this. 
responses = {
    "hi": "Hello!", 
    "weather": "I can't tell you the weather, I'm not that clever",
    "help": "Sure what do you need?",
    "robot": "I'm not a robot, I'm a simple Python Chatbot"
}

#The 'brains of our chatbot'
def chatbot(message): 
    msg = message.lower() #converts message parameter (our user input later) to lower case.

#for loop to assign temp variables (keyword and reply to the keys and values in our dictionary)
    for keyword, reply in responses.items():
        if keyword in msg: #if the keyword is in our user input it will return reply. 
            return reply

    return "Hmm I don't know how to respond."  #else it will return confusion.

while True: #Simple event loop to keep the code running.
    user_input = input("You: ")
    if user_input == "quit":
        break

    print(f"Bot: {chatbot(user_input)}") #Calls our chatbot function if the user types anything other than quit. 
