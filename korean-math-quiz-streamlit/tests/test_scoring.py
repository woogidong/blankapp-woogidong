import pytest
from src.utils.scorer import calculate_score, identify_weak_areas

def test_calculate_score():
    # Test case 1: All correct answers
    answers = [True, True, True]
    assert calculate_score(answers) == 100

    # Test case 2: One incorrect answer
    answers = [True, False, True]
    assert calculate_score(answers) == 66.67

    # Test case 3: All incorrect answers
    answers = [False, False, False]
    assert calculate_score(answers) == 0

def test_identify_weak_areas():
    # Test case 1: No incorrect answers
    user_answers = [True, True, True]
    questions = ['Q1', 'Q2', 'Q3']
    assert identify_weak_areas(user_answers, questions) == []

    # Test case 2: Some incorrect answers
    user_answers = [True, False, True]
    questions = ['Q1', 'Q2', 'Q3']
    assert identify_weak_areas(user_answers, questions) == ['Q2']

    # Test case 3: All incorrect answers
    user_answers = [False, False, False]
    questions = ['Q1', 'Q2', 'Q3']
    assert identify_weak_areas(user_answers, questions) == ['Q1', 'Q2', 'Q3']