import json
from pathlib import Path
import random
from datetime import datetime


class MVQuestionGenerator:

    format_date = classmethod
    format_q_object = classmethod
    fetch_all_mvs = classmethod

    title_q = classmethod
    release_date_q = classmethod
    artist_q = classmethod

    def __init__(self):
        pass

    def format_date(self, date):
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        return str(date_obj)

    def format_q_object(self, question, groups, answers, right_ans_idx):
        question = {
            'question': question,
            'groups': groups,
            'answers': answers,
            'right_ans_idx': right_ans_idx
        }
        return question

    def fetch_all_mvs(self, gender):
        data_path = ""

        path = Path(__file__)

        if gender == "bg" or gender == "gg":
            data_path = path.parent.parent.parent

        with open(data_path.as_uri().removeprefix('file:///') + f'/data/mvs/{gender}_mvs.json', 'r') as db:
            data = json.load(db)
            return data

    def title_q(self, data):
        answers = [0] * 4
        mv_idx = random.randint(0, len(data))
        right_ans_idx = random.randint(0, 3)

        right_mv = data[str(mv_idx)]
        print(right_mv)


qgen = MVQuestionGenerator()
data = qgen.fetch_all_mvs('bg')
qgen.title_q(data)
