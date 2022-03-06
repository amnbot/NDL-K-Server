import json
from pathlib import Path
import random
from datetime import datetime


class IdolQuestionGenerator:

    format_q_object = classmethod
    fetch_all_groups = classmethod

    birthyear_q = classmethod
    korean_name_q = classmethod
    group_q = classmethod

    def __init__(self):
        pass

    def format_q_object(self, question, idols, answers, right_ans_idx):
        question = {
            'question': question,
            'idols': idols,
            'answers': answers,
            'right_ans_idx': right_ans_idx
        }
        return question

    def fetch_all_idols(self, gender):
        data_path = ""

        path = Path(__file__)

        if gender == "male" or gender == "female":
            data_path = path.parent.parent.parent
            # data_path.chmod(0o444)
            #data_path = f"D:/VStudio/Projects/Web/WebScraping/KpopDatabase/data/idols/{gender}_groups.json"

        with open(data_path.as_uri().removeprefix('file:///') + f'/data/idols/{gender}_idols.json', 'r') as db:
            data = json.load(db)
            return data

    def birthyear_q(self, data):
        answers = [0] * 4
        idol_idx = random.randint(0, len(data))
        right_ans_idx = random.randint(0, 3)

        right_idol = data[str(idol_idx)]

        birth_ans = right_idol["Date Of Birth"]

        answers[right_ans_idx] = birth_ans.split('-')[0]

        for i in range(0, 4):
            if i != right_ans_idx:
                wrong_ans = random.choice(
                    [i for i in range(1985, 2005) if i not in answers])
                answers[i] = wrong_ans

        for i in answers:
            print(i)

        question = f"What year was {right_idol['Stage Name']} ({right_idol['Group']}) born?"

        if right_idol["Group"] == "":
            question = f"What year was {right_idol['Stage Name']} born?"

        return self.format_q_object(question, None, answers, right_ans_idx)

    def korean_name_q(self, data):
        indices = [0] * 4
        answers = [0] * 4
        for i in range(0, 4):
            idx = random.choice(
                [i for i in range(len(data)) if i not in indices and data[str(i)]["Full Name"] != ""])
            indices[i] = idx
            answers[i] = data[str(idx)]["Full Name"]

        right_ans_idx = random.randint(0, 3)

        right_idol = data[str(indices[right_ans_idx])]

        question = f"What is {right_idol['Stage Name']}'s ({right_idol['Group']}) full name?"
        if right_idol["Group"] == "":
            question = f"What is {right_idol['Stage Name']}'s full name?"

        return self.format_q_object(question, None, answers, right_ans_idx)

    def group_q(self, data):
        indices = [0] * 4
        answers = [0] * len(indices)

        for i in range(0, 4):
            idx = random.choice([i for i in range(
                len(data)) if i not in indices and data[str(i)]["Group"] != "" and data[str(i)]["Group"] not in answers])
            indices[i] = idx
            answers[i] = data[str(idx)]["Group"]

        right_ans_idx = random.randint(0, 3)

        right_idol = data[str(indices[right_ans_idx])]

        question = f"Which of these groups is {right_idol['Stage Name']} a member of?"

        return self.format_q_object(question, None, answers, right_ans_idx)

    def fandom_name_q(self, data):
        indices = random.sample(range(len(data)), 4)
        groups = [0] * len(indices)
        answers = [0] * len(indices)

        for i in range(len(indices)):
            group = data[str(indices[i])]

            while group["FanClub"] == "":
                new_idx = random.choice(
                    [i for i in range(len(data)) if i not in indices])
                indices[i] = new_idx
                group = data[str(indices[i])]

            groups[i] = group
            answers[i] = group["FanClub"]

        right_ans_idx = random.randint(0, 3)
        right_group = groups[right_ans_idx]

        question = f"What is {right_group['Name']}'s ({right_group['Short Name']}) fandom name?"
        if not right_group["Short Name"]:
            question = f"What is {right_group['Name']}'s fandom name?"

        return self.format_q_object(question, groups, answers, right_ans_idx)


qgen = IdolQuestionGenerator()
data = qgen.fetch_all_idols('male')
resp = qgen.group_q(data)
# print(resp)
# qgen.company_q(data)
