import json
from pathlib import Path
import random
from datetime import datetime


class GroupQuestionGenerator:

    format_date = classmethod
    format_q_object = classmethod
    fetch_all_groups = classmethod
    debut_q = classmethod
    current_members_q = classmethod
    original_members_q = classmethod
    fandom_name_q = classmethod
    korean_name_q = classmethod

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

    def fetch_all_groups(self, gender):
        data_path = ""

        path = Path(__file__)

        if gender == "boy" or gender == "girl":
            data_path = path.parent.parent.parent
            # data_path.chmod(0o444)
            #data_path = f"D:/VStudio/Projects/Web/WebScraping/KpopDatabase/data/groups/{gender}_groups.json"

        with open(data_path.as_uri().removeprefix('file:///') + f'/data/groups/{gender}_groups.json', 'r') as db:
            data = json.load(db)
            return data

    def debut_q(self, data):
        indices = random.sample(range(len(data)), 4)
        # print(indices)
        groups = [0] * len(indices)
        answers = [0] * len(indices)

        group_idx = random.randint(0, len(data))
        right_ans_idx = random.randint(0, 3)

        right_group = data[str(group_idx)]

        debut_ans = right_group["Debut"]

        answers[right_ans_idx] = debut_ans.split('-')[0]

        for i in range(0, 4):
            if i != right_ans_idx:
                wrong_ans = random.choice(
                    [i for i in range(1995, 2022) if i not in answers])
                answers[i] = wrong_ans

        for i in answers:
            print(i)

        """for i in range(len(indices)):
            group = data[str(indices[i])]
            # str_date = group['Debut']
            # group['Debut'] = self.format_date(str_date)
            groups[i] = group
            answers[i] = group['Debut']"""

        question = f"What year did {right_group['Name']} ({right_group['Short Name']}) make their debut?"
        if not right_group["Short Name"]:
            question = f"What year did {right_group['Name']} make their debut?"

        return self.format_q_object(question, groups, answers, right_ans_idx)

    def current_members_q(self, data):
        groups = [0] * 4
        answers = [0] * 4

        group_idx = random.randint(0, len(data))
        right_ans_idx = random.randint(0, 3)

        right_group = data[str(group_idx)]

        answers[right_ans_idx] = int(right_group['Current Member Count'])

        for i in range(0, 4):
            if i != right_ans_idx:
                wrong_ans = random.choice(
                    [i for i in range(2, 14) if i not in answers])
                answers[i] = wrong_ans

        question = f"How many members does {right_group['Name']} ({right_group['Short Name']}) currently have?"
        if not right_group["Short Name"]:
            question = f"How many members does {right_group['Name']} currently have?"

        return self.format_q_object(question, groups, answers, right_ans_idx)

    def original_members_q(self, data):
        groups = [0] * 4
        answers = [0] * 4

        group_idx = random.randint(0, len(data))
        right_ans_idx = random.randint(0, 3)

        right_group = data[str(group_idx)]

        answers[right_ans_idx] = int(right_group['Original Member Count'])

        for i in range(0, 4):
            if i != right_ans_idx:
                wrong_ans = random.choice(
                    [i for i in range(2, 14) if i not in answers])
                answers[i] = wrong_ans

        question = f"How many members did {right_group['Name']} ({right_group['Short Name']}) originally have?"
        if not right_group["Short Name"]:
            question = f"How many members did {right_group['Name']} originally have?"

        return self.format_q_object(question, groups, answers, right_ans_idx)

    def company_q(self, data):
        indices = random.sample(range(len(data)), 4)
        groups = [0] * len(indices)
        answers = [0] * len(indices)

        group_idx = random.randint(0, len(data))
        right_ans_idx = random.randint(0, 3)

        right_group = data[str(group_idx)]

        answers[right_ans_idx] = right_group['Company']

        for i in range(len(indices)):
            if i != right_ans_idx:
                while data[str(indices[i])] == answers[right_ans_idx]:
                    new_idx = random.choice(
                        [i for i in range(len(data)) if i not in indices and data[str(indices[i])]["Company"] not in answers])
                    indices[i] = new_idx

            answers[i] = data[str(indices[i])]["Company"]

        print(str(answers))

        question = f"Which company owns {right_group['Name']} ({right_group['Short Name']})?"
        if not right_group["Short Name"]:
            question = f"Which company owns {right_group['Name']}?"

        return self.format_q_object(question, groups, answers, right_ans_idx)

    def korean_name_q(self, data):
        indices = random.sample(range(len(data)), 4)
        groups = [0] * len(indices)
        answers = [0] * len(indices)

        for i in range(len(indices)):
            group = data[str(indices[i])]

            while group["Korean Name"] == "":
                new_idx = random.choice(
                    [i for i in range(len(data)) if i not in indices])
                indices[i] = new_idx
                group = data[str(indices[i])]
            groups[i] = group
            answers[i] = group['Korean Name']

        right_ans_idx = random.randint(0, 3)
        right_group = groups[right_ans_idx]

        question = f"What is {right_group['Name']}'s ({right_group['Short Name']}) korean name?"
        if not right_group["Short Name"]:
            question = f"What is {right_group['Name']}'s korean name?"

        return self.format_q_object(question, groups, answers, right_ans_idx)

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


qgen = GroupQuestionGenerator()
data = qgen.fetch_all_groups('boy')
# print(data)
# qgen.company_q(data)
