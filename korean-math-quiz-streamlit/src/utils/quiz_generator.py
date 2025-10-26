from random import sample
import json

def load_questions(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_quiz(num_questions, curriculum_file, questions_file):
    curriculum = load_questions(curriculum_file)
    questions = load_questions(questions_file)

    # Filter questions based on curriculum topics
    filtered_questions = [q for q in questions if q['topic'] in curriculum['topics']]
    
    # Randomly sample questions for the quiz
    quiz_questions = sample(filtered_questions, min(num_questions, len(filtered_questions)))
    
    return quiz_questions

def identify_weak_areas(user_answers, correct_answers):
    weak_areas = {}
    
    for question_id, user_answer in user_answers.items():
        if user_answer != correct_answers[question_id]:
            topic = correct_answers[question_id]['topic']
            if topic in weak_areas:
                weak_areas[topic] += 1
            else:
                weak_areas[topic] = 1
                
    return weak_areas

def get_quiz_summary(user_answers, correct_answers):
    score = sum(1 for q_id in user_answers if user_answers[q_id] == correct_answers[q_id])
    total_questions = len(correct_answers)
    return {
        'score': score,
        'total': total_questions,
        'weak_areas': identify_weak_areas(user_answers, correct_answers)
    }