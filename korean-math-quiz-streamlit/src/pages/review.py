from streamlit import st
import json

def load_questions():
    with open('src/data/questions/sample_questions.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def display_review(answers, questions):
    for question in questions:
        question_text = question['question']
        correct_answer = question['answer']
        user_answer = answers.get(question['id'], None)

        st.write(f"**Question:** {question_text}")
        if user_answer is None:
            st.write("You did not answer this question.")
        else:
            st.write(f"**Your Answer:** {user_answer}")
            if user_answer == correct_answer:
                st.success("Correct!")
            else:
                st.error(f"Incorrect! The correct answer is: {correct_answer}")
                st.write(f"**Explanation:** {question.get('explanation', 'No explanation available.')}")

def main():
    st.title("Quiz Review")
    st.write("Review your answers and see where you can improve.")

    # Assuming answers are stored in session state
    if 'answers' in st.session_state:
        answers = st.session_state.answers
        questions = load_questions()
        display_review(answers, questions)
    else:
        st.write("No quiz answers found. Please take a quiz first.")

if __name__ == "__main__":
    main()