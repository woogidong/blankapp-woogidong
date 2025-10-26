from typing import Dict, List
import json

class CurriculumMapper:
    def __init__(self, middle_school_path: str, high_school_path: str):
        self.middle_school_curriculum = self.load_curriculum(middle_school_path)
        self.high_school_curriculum = self.load_curriculum(high_school_path)

    def load_curriculum(self, path: str) -> Dict:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def map_questions_to_curriculum(self, questions: List[Dict]) -> Dict[str, List[Dict]]:
        mapped_questions = {
            "middle_school": [],
            "high_school": []
        }

        for question in questions:
            topic = question.get("topic")
            if topic in self.middle_school_curriculum.get("topics", []):
                mapped_questions["middle_school"].append(question)
            elif topic in self.high_school_curriculum.get("topics", []):
                mapped_questions["high_school"].append(question)

        return mapped_questions

    def identify_weak_areas(self, incorrect_answers: List[Dict]) -> Dict[str, List[Dict]]:
        weak_areas = {
            "middle_school": [],
            "high_school": []
        }

        for answer in incorrect_answers:
            topic = answer.get("topic")
            if topic in self.middle_school_curriculum.get("topics", []):
                weak_areas["middle_school"].append(answer)
            elif topic in self.high_school_curriculum.get("topics", []):
                weak_areas["high_school"].append(answer)

        return weak_areas