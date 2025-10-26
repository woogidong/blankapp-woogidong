import pytest
from src.utils.quiz_generator import generate_quiz
from src.data.questions.sample_questions import sample_questions

def test_generate_quiz():
    # Test generating a quiz with a specific number of questions
    num_questions = 5
    quiz = generate_quiz(sample_questions, num_questions)
    
    assert len(quiz) == num_questions, "Quiz should contain the specified number of questions"
    for question in quiz:
        assert 'question' in question, "Each quiz question should have a 'question' key"
        assert 'options' in question, "Each quiz question should have an 'options' key"
        assert 'answer' in question, "Each quiz question should have an 'answer' key"

def test_generate_quiz_with_invalid_number():
    # Test generating a quiz with an invalid number of questions
    num_questions = 0
    quiz = generate_quiz(sample_questions, num_questions)
    
    assert quiz == [], "Quiz should be empty when number of questions is zero"

def test_generate_quiz_exceeds_available_questions():
    # Test generating a quiz that exceeds the number of available questions
    num_questions = 100  # Assuming there are less than 100 questions in sample_questions
    quiz = generate_quiz(sample_questions, num_questions)
    
    assert len(quiz) <= len(sample_questions), "Quiz should not exceed the number of available questions"