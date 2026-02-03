from sklearn.feature_extraction.text import TfidfVectorizer #Turns text into numbers so computer can understand
from sklearn.metrics.pairwise import cosine_similarity #measures similarity of text
import random


training_data = {
    "hi": "Hello!",
    "hello": "Hello!",
    "hey": "Hello!",
    "what's the weather": "I can't tell you the weather, I'm not that clever",
    "tell me the weather": "I can't tell you the weather, I'm not that clever",
    "help me": "Sure, what do you need?",
    "i need help": "Sure, what do you need?",
    "are you a robot": "I'm not a robot, I'm a simple Python chatbot",
    "are you human": "I'm not a robot, I'm a simple Python chatbot"
}


vectorizer = TfidfVectorizer()
replies = vectorizer.fit_transform(training_sentences) #Allows us to convert our training data to a number using indexes (vectors)

#chatbots brain
def chatbot(message): 
    msg_vec = vectorizer.transform([message]) #converts your message to a vector
    similarity = cosine_similarity(msg_vec, replies) #checks the similarity of your message vector and gives a score on how close message and training message are. 
    best_match = similarity.argmax() #picks the training message with the most similarity to your message. 

    if similarity[0][best_match] < 0.2:
        return "Hmm, I don't know how to respond."

    return responses[best_match]

while True: #Simple event loop to keep the code running.
    user_input = input("You: ")
    if user_input == "quit":
        break

    print(f"Bot: {chatbot(user_input)}") #Calls our chatbot function if the user types anything other than quit. 

    #Add more training data: training_data["tell me a joke"] = "I would, but my humour module is still loading."
    #downlaod module in virtual environment and import with pip install scikit-learn
