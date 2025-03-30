import nltk
from nltk.chat.util import Chat, reflections


messages = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you?", ["I'm doing well, how about you?", "I'm just a bot, but I'm good!"]),
    (r"what is your name?|who are you?", ["I'm a LousyAI!", "Call me Lousy."]),
    (r"bye", ["Goodbye!", "See you later!","Take Care"]),
]


chatbot = Chat(messages, reflections)

def start_chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    chatbot.converse()

if __name__ == "__main__":
    start_chat()
