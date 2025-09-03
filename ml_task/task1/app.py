import streamlit as st

api_key = "TEST" # TBF

def text_processor(uploaded_file):
    text = uploaded_file.read().decode("utf-8")
    words = text.split()
    chunks = [" ".join(words[i:i + 100]) for i in range(0, len(words), 100)]

def submit_prompt():
    pass

st.title(" Document-Grounded Chatbot")

# Upload File´
uploaded_file = st.file_uploader("Choose a file (.txt / .md)", type=("txt", "md"))
if uploaded_file is not None:
    text_processor(uploaded_file)

# Chat Area
question = st.text_input("Enter your question: 👇",
                        disabled=not uploaded_file,
)

if uploaded_file and question and not api_key:
    st.error("Error with API Key")

# Ask Button
bu = st.button("Ask", type="primary")

if bu: # If Clicked
    if not question:
        st.error("Please Provide your question")

    if uploaded_file and question and api_key: 
        results = submit_prompt()
        
