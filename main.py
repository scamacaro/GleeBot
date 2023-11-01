""" Sanyerlis Camacaro - CSC370 - Sancamac@uat.edu Assignment: Assignment 5.1: Final Project Code Deliverable

"GleeBot Chat Bot"

GleeBot is designed to have interactive conversations with you. 
You can ask it questions, have a friendly chat, or seek assistance on various topics. 
GleeBot can tell you about its favorite soccer player (Messi), its favorite hobby (digital AI art), and who inspires it (Picasso). 
It's like having a friendly digital companion to talk to and get information from. 
Feel free to start a conversation and explore what GleeBot can do!

Requirements and Expectations:
You may choose to do a Python, AI, or ML application.
You may design and choose what the application does.
This project must technically demonstrate Python or AI, or Machine Learning.
It must also do something clever, not complex.
This project should have a purpose and a theme that should match. 
Code must be commented well, maintainable, and named well.
The project must have a great User Experience (UX).
"""
# Import necessary modules
import tkinter as tk
from nltk.chat.util import Chat, reflections

# These are the patterns and responses that GleeBot will use in conversations.
pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today?",]
    ],
    [
        r"(.*)help(.*)",
        ["I can help you with various questions and have a friendly chat. Just ask me anything!",]
    ],
    [
        r"(.*) your name ?",
        ["My name is GleeBot, but you can just call me Glee and I'm here to chat and assist you.",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "I am great!"]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "It's OK, never mind that.",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that", "Alright, great!"]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*)created(.*)",
        ["Sanyerlis Camacaro created me using Python Programming Language.", "Top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Denver, Colorado',]
    ],
    [
        r"(.*)snowing in (.*)",
        ["Yes, it's snowing in %2. Enjoy the snow!",]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health.",]
    ],
    [
        r"(.*) (favorite|favourite) (soccer|football) (player|star)?",
        ["My favorite soccer player is Messi.", "I admire Messi as a soccer player.",]
    ],
    [
        r"what is your favorite hobby?",
        ["My favorite hobby is creating digital AI art.", "I love digital AI art.",]
    ],
    [
        r"who inspires you to create?",
        ["I'm inspired by artists like Picasso.", "Picasso is one of my inspirations.",]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :)", "It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ["I'm here to chat and assist you. You can ask me questions or simply have a conversation. How can I help you today?"]
    ],
]

# Create a reflection dictionary
my_dummy_reflections = {
    "go": "gone",
    "hello": "hey there"
}

# Initialize the chatbot
chatbot = Chat(pairs, reflections)

# Function to send a user message and receive a response
def send_message():
    user_input = entry.get()
    response = chatbot.respond(user_input)
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, "You: " + user_input + "\n", "user")
    chat_history.insert(tk.END, "GleeBot: " + response + "\n", "bot")
    chat_history.config(state=tk.DISABLED)
    entry.delete(0, tk.END)

# Create the main chat window
root = tk.Tk()
root.title("GleeBot Chat")
root.geometry("400x400")

# Create a frame to hold the chat history
chat_frame = tk.Frame(root)
chat_frame.pack(fill=tk.BOTH, expand=True)

# Create a scrollbar for the chat history
scrollbar = tk.Scrollbar(chat_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a text widget to display the chat history
chat_history = tk.Text(chat_frame, wrap=tk.WORD, yscrollcommand=scrollbar.set)
chat_history.tag_configure("user", foreground="blue")
chat_history.tag_configure("bot", foreground="green")
chat_history.pack(fill=tk.BOTH, expand=True)
chat_history.config(state=tk.DISABLED)

scrollbar.config(command=chat_history.yview)

# Create an entry widget for user input
entry = tk.Entry(root)
entry.pack(fill=tk.X)

# Create a send button to send user input
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

# Function to send a message when the user presses the Enter key
def on_enter(event):
    send_message()

root.bind("<Return>", on_enter)

# Start the main loop
root.mainloop()
