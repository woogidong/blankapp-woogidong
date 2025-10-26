from streamlit import button, text_input, selectbox, markdown, container

def render_quiz_ui():
    with container():
        markdown("## Math Quiz")
        name = text_input("Enter your name:")
        grade = selectbox("Select your grade:", ["Middle School", "High School"])
        start_quiz_button = button("Start Quiz")

        if start_quiz_button:
            if name and grade:
                markdown(f"Welcome, {name}! You are in {grade}. Let's start the quiz!")
            else:
                markdown("Please enter your name and select your grade to start the quiz.")

def render_review_ui(incorrect_answers):
    with container():
        markdown("## Review Your Answers")
        if incorrect_answers:
            for question, user_answer, correct_answer in incorrect_answers:
                markdown(f"**Question:** {question}")
                markdown(f"**Your Answer:** {user_answer}")
                markdown(f"**Correct Answer:** {correct_answer}")
                markdown("---")
        else:
            markdown("You answered all questions correctly!")

def render_analytics_ui(performance_data):
    with container():
        markdown("## Performance Analytics")
        if performance_data:
            for topic, score in performance_data.items():
                markdown(f"**Topic:** {topic} - **Score:** {score}%")
        else:
            markdown("No performance data available.")