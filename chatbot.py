import os
import ssl
import random
import nltk
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# -------------------------------
# Fix SSL & NLTK setup
# -------------------------------
ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("nltk_data"))
nltk.download("punkt", quiet=True)

# -------------------------------
# Training data with small talk
# -------------------------------
training_data = {
    "greetings": {
        "patterns": ["Hi","hi" "Hello","hello","hey", "Hey", "Good morning"],
        "responses": ["Hello {name}!", "Hi there 👋", "Hey! How are you today?", "Good morning ☀️"]
    },
    "goodbye": {
        "patterns": ["Bye", "See you later", "Goodbye"],
        "responses": ["Goodbye! 👋", "See you later, {name}!", "Take care!"]
    },
    "thanks": {
        "patterns": ["Thank you", "Thanks", "Thank you so much"],
        "responses": ["You're welcome 😊", "No problem, {name}!", "Glad I could help!"]
    },
    "name": {
        "patterns": ["What's your name?", "Who are you?", "Tell me your name"],
        "responses": ["I am your friendly chatbot 🤖"]
    },
    "how_are_you": {
        "patterns": ["How are you?", "What's up?", "How's it going?"],
        "responses": ["I'm doing great, thanks for asking! How about you?", 
                      "Pretty good! What about you?", 
                      "I'm always happy to chat! How are you feeling today?"]
    },
    "hobbies": {
        "patterns": ["What do you do for fun?", "Do you have hobbies?", "What are your interests?"],
        "responses": ["I love chatting with people like you 🤗", 
                      "I enjoy learning new words every day!", 
                      "My hobby is making conversations fun!"]
    },
    "how_are_you": {
        "patterns": [
            "How are you",
            "how are you?",
            "how r u",
            "how's it going",
            "what's up",
            "how do you do",
            "how are things",
            "how are you doing",
            "are you okay"
        ],
        "responses": [
            "I'm doing great, thanks for asking! How about you?",
            "Pretty good! What about you?",
            "I'm always happy to chat! How are you feeling today?"
        ]
    },
    "default": {
        "responses": [
            "Hmm, I’m not sure I understood that 🤔. Can you rephrase?",
            "Interesting! Tell me more about that.",
            "That’s cool! Could you explain it a bit more?"
        ]
    }
}

# -------------------------------
# Prepare dataset
# -------------------------------
patterns = []
labels = []

for intent, intent_data in training_data.items():
    if "patterns" in intent_data:
        for pattern in intent_data["patterns"]:
            patterns.append(pattern)
            labels.append(intent)

vectorizer = TfidfVectorizer(
    tokenizer=nltk.word_tokenize,
    token_pattern=None,
    lowercase=True,
    #stop_words="english"
)

X = vectorizer.fit_transform(patterns)
model = LogisticRegression(max_iter=1000)
model.fit(X, labels)

# -------------------------------
# Chatbot logic
# -------------------------------
def chatbot_response(user_input, username="Friend", threshold=0.4):
    """Generate conversational chatbot response with context awareness."""
    X_test = vectorizer.transform([user_input])
    probs = model.predict_proba(X_test)[0]
    intent_idx = probs.argmax()
    confidence = probs[intent_idx]

    predicted_intent = model.classes_[intent_idx]

    # If confidence is low → fallback
    if confidence < threshold:
        return random.choice(training_data["default"]["responses"])

    # Pick response and personalize
    responses = training_data[predicted_intent]["responses"]
    reply = random.choice(responses)
    return reply.format(name=username)

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="Conversational Chatbot", page_icon="🤖")
st.title("💬 Conversational Chatbot")

# Store chat history
if "history" not in st.session_state:
    st.session_state.history = []
if "username" not in st.session_state:
    st.session_state.username = "Friend"

# Ask username once
if len(st.session_state.history) == 0:
    st.session_state.username = st.text_input("What's your name?", "Friend")

# Chat input
user_input = st.chat_input("Type your message here...")

if user_input:
    reply = chatbot_response(user_input, st.session_state.username)
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", reply))

# Display chat
for sender, message in st.session_state.history:
    if sender == "You":
        st.markdown(f"**👤 {st.session_state.username}:** {message}")
    else:
        st.markdown(f"**🤖 Bot:** {message}")
