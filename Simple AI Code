#Function that normalises (sets user input to lower case) user input and sets defines response conditions and  AI 'logic'
def simple_ai(user_input):
    user_input = user_input.lower()

#Conditionals that act as logic for the AI
    if "hello" in user_input or "hi" in user_input:
        return "Hi there!"
    elif "weather" in user_input:
        return "I can't check weather, but I hope it's nice!"
    elif "bye" in user_input:
        return "Goodbye!"
    elif "cheese" in user_input:
        return "Cheese is good!"
    else:
        return "I'm not sure how to respond to that."

#event loop saying to ask for text and if  the user enters quit, leave the loop and quit the program. 
while True:
    text = input("You: ")
    if text.lower() == "quit":
        break
    else:
        print("AI:", simple_ai(text))
