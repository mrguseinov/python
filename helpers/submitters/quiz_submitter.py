from __future__ import annotations

from helpers.submitters.submitter import Submitter
from helpers.widgets import MyCheckBoxes, MyRadioButtons

_ALL_ANSWERS = {
    "01": [2, 1, 2, 1, 4, 4, 3, 3, 2, 1],
    "02": [3, 1, 4, 1, 1, 4, 4, 4, 4, 1],
    "03": [4, 3, 1, 3, 2, 1, 4, 1, 1, 2],
    "04": [4, 2, 2, 3, 1, 1, 1, 1, 1, 1],
    "05": [1, 2, 2, 4, 1, 4, 1, [1, 3], 2, 1],
    "06": [1, 2, 5, 1, 3, 1, 4, 1, 2, 1],
    "07": [4, 1, 4, 1, 2, 4, 4, 4, 2, 2],
    "08": [3, 4, 3, 2, 3, 4, 6, 3, 2, 3],
    "09": [1, 4, 3, 1, 1, 4, 3, 3, 5, 4],
    "10": [4, 4, 1, 4, 2, 3, 4, 4, 1, 2],
    "11": [1, 1, 2, 1, 1, 1, 5, 5, 5, 5],
    "12.1": [5, 5, 3, 1, 1, 4, 2, 4, 1, 1],
    "12.2": [1, 1, 1, 1, 2, 2, 3, 1, 2, 2, 4, 3, 4],
    "13.1": [2, [1, 4, 5], [2, 3], [1, 5], 4, 2, 2, 2, 1, 4],
    "13.2": [4, 4, 2, 1, 4, 2, 2, [1, 2, 3, 4], 5, 4],
    "14": [1, 1, 3, 4, 2, 3, 5, 2, 4, 1, 2],
    "15.1": [[1, 3, 4], 3, 2, 1, 2, 3, 1, 5, 3, 4, 3],
    "15.2": [5, 2, 3, 5, 2, 5, 3, 4, 2, 1],
    "15.3": [4, 3, 4, 2, 1, 1, 4, 1, 2],
}


class QuizSubmitter(Submitter):
    def __init__(self, quiz_id: str) -> None:
        self._quiz_answers = _ALL_ANSWERS[quiz_id]

    def submit(self, questions: list[MyCheckBoxes] | list[MyRadioButtons]) -> None:
        for id, question in enumerate(questions):
            if question.is_answer_correct(self._quiz_answers[id]):
                self._show_message(f"Question {id}: Right.", "green")
            else:
                self._show_message(f"Question {id}: Wrong.", "red")
