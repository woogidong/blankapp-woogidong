class UserProgress:
    def __init__(self):
        self.scores = []
        self.incorrect_answers = {}
    
    def add_score(self, score):
        self.scores.append(score)
    
    def record_incorrect_answer(self, question_id, correct_answer):
        if question_id not in self.incorrect_answers:
            self.incorrect_answers[question_id] = correct_answer
    
    def get_average_score(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)
    
    def get_weak_areas(self):
        return self.incorrect_answers.keys()