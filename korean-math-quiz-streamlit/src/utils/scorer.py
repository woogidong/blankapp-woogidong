def calculate_score(user_answers, correct_answers):
    score = 0
    incorrect_answers = []

    for question_id, user_answer in user_answers.items():
        if user_answer == correct_answers.get(question_id):
            score += 1
        else:
            incorrect_answers.append(question_id)

    return score, incorrect_answers


def identify_weak_areas(incorrect_answers, curriculum_data):
    weak_areas = {}

    for question_id in incorrect_answers:
        topic = curriculum_data.get(question_id, {}).get('topic')
        if topic:
            if topic not in weak_areas:
                weak_areas[topic] = 0
            weak_areas[topic] += 1

    return weak_areas