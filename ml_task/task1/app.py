import streamlit as st

def text_processor(uploaded_file):
    text = uploaded_file.read().decode("utf-8")
    words = text.split()
    chunks = [" ".join(words[i:i + 100]) for i in range(0, len(words), 100)]

def submit_prompt():
    pass

st.title(" Document-Grounded Chatbot")

# Upload File´
uploaded_file = st.file_uploader("Choose a file (.txt / .md)")
if uploaded_file is not None:
    text_processor(uploaded_file)

# Chat Area
title = st.text_input("Enter your question: 👇")

# Ask Button
bu = st.button("Ask", type="primary")

if bu: # If Clicked
    results = submit_prompt()
