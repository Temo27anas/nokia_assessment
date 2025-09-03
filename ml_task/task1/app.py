import streamlit as st
from functions import pipeline 


api_key = "TEST" # TBF

def read_text(uploaded_file):
    text = uploaded_file.read().decode("utf-8")
    return text

def submit_prompt():
    pass

st.title(" Document-Grounded Chatbot")

# Upload File
uploaded_file = st.file_uploader("Choose a file (.txt / .md)", type=("txt", "md"))

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
        file_content = read_text(uploaded_file)
        with st.spinner("Wait for it...", show_time=True):
            results = pipeline(file_content, question)
            st.success("Done!")
            st.subheader("Answer:")
            st.write(results["answer"])

            st.subheader("Citations:")
            for citation in results["citations"]:
                st.write(citation)



        
