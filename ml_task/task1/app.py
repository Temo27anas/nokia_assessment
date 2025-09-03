import streamlit as st
from functions import pipeline 

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

# Ask Button
bu = st.button("Ask", type="primary")

if bu: # If Clicked
    if not uploaded_file:
        st.error("Error with provided file")
    if not question:
        st.error("Please Provide your question")

    if uploaded_file and question: 
        results = submit_prompt()
        file_content = read_text(uploaded_file)

        with st.spinner("Wait for it...", show_time=True):
            results = pipeline(file_content, question)

            if results is None:
                st.error("Error in the Answer generation process")

            elif "NOT FOUND" in results :
                st.info("No Relevant Answer Found!")

            else:
                st.success("Done!")
                st.subheader("Answer:")
                st.write(results["answer"])

                st.subheader("Citations:")
                for citation in results["citations"]:
                    st.write(citation)



        
