import random

intents = {
    "greeting": {
        "keywords": ["hi", "hello", "hey", "hiya", "yo"],
        "responses": ["Hello!", "Hey there!", "Hi!", "Greetings!", "Nice to see you!"]
    },
    "weather": {
        "keywords": ["weather", "rain", "sunny"],
        "responses": ["I can't tell you the weather, I'm not that clever"]
    },
    "help": {
        "keywords": ["help", "assist", "support"],
        "responses": ["Sure, what do you need?", "I'm here to help!"]
    },
    "robot": {
        "keywords": ["robot", "bot", "android"],
        "responses": ["I'm not a robot, I'm a simple Python chatbot"]
    }
}

def chatbot(message):
    msg = message.lower()

    for intent, data in intents.items():
        if any(keyword in msg for keyword in data["keywords"]):
            return random.choice(data["responses"])

    return "Hmm, I don't know how to respond."

while True: #Simple event loop to keep the code running.
    user_input = input("You: ")
    if user_input == "quit":
        break

    print(f"Bot: {chatbot(user_input)}") #Calls our chatbot function if the user types anything other than quit. 