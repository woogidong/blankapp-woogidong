import streamlit as st

def home():
    st.title("Welcome to the Korean Math Quiz App")
    st.write("This application is designed to help middle and high school students in South Korea improve their math skills through quizzes.")
    
    st.header("Navigation")
    st.write("Use the links below to navigate to different sections of the app:")
    
    if st.button("Start Quiz"):
        st.session_state.page = "quiz"
    
    if st.button("Review Answers"):
        st.session_state.page = "review"
    
    if st.button("View Analytics"):
        st.session_state.page = "analytics"

if __name__ == "__main__":
    home()