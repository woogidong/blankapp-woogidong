import streamlit as st
from pages import home, quiz, review, analytics

def main():
    st.set_page_config(page_title="Korean Math Quiz", layout="wide")
    
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    options = ["Home", "Quiz", "Review", "Analytics"]
    selection = st.sidebar.radio("Go to", options)

    # Page routing
    if selection == "Home":
        home.show()
    elif selection == "Quiz":
        quiz.show()
    elif selection == "Review":
        review.show()
    elif selection == "Analytics":
        analytics.show()

if __name__ == "__main__":
    main()