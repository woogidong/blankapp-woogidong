from streamlit import st
import json
from src.utils.quiz_generator import generate_quiz
from src.utils.scorer import calculate_score
from src.models.user_progress import UserProgress

# Load sample questions
with open('src/data/questions/sample_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# Initialize user progress
user_progress = UserProgress()

def display_quiz():
    st.title("Math Quiz")
    st.write("Answer the following questions based on the South Korean middle and high school curriculum.")

    score = 0
    total_questions = len(questions)
    user_answers = []

    for question in questions:
        st.subheader(question['question'])
        user_answer = st.radio("Select your answer:", question['options'])
        user_answers.append(user_answer)

        if user_answer == question['correct_answer']:
            st.success("Correct!")
            score += 1
        else:
            st.error(f"Incorrect! The correct answer is: {question['correct_answer']}")

    # Calculate and display score
    st.write(f"You scored {score} out of {total_questions}.")
    user_progress.update_progress(score, total_questions)

if __name__ == "__main__":
    display_quiz()