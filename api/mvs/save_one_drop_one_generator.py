import json
from pathlib import Path
import random
from datetime import datetime
from mvs.mvs_recommender import MvsRecommender as mvr

class SODOGenerator:

    format_object = classmethod
    fetch_all_mvs = classmethod

    def fetch_all_mvs(self):
        data_path = ""
        data = [0] * 2

        path = Path(__file__)

        data_path = path.parent.parent.parent

        with open(data_path.as_uri().removeprefix('file:///') + f'/data/mvs/bg_mvs.json', 'r') as db:
            data[0] = json.load(db)
        with open(data_path.as_uri().removeprefix('file:///') + f'/data/mvs/gg_mvs.json', 'r') as db:
            data[1] = json.load(db)

        return data

    def format_object(self, choices):
        choices = {
            'one': choices[0],
            'two': choices[1]
        }
        return choices

    def generate_sodo(self, data):
        genders = random.sample(range(0, 2), 2)

        indices = [0] * 2
        choices = [0] * 2

        for i in range(len(genders)):
            mvs = data[genders[i]]
            mv_idx = -1
            if genders[0] == genders[1]:
                mv_idx = random.choice(
                    [j for j in range(len(mvs) - 1) if j not in indices])
            else:
                mv_idx = random.randint(0, len(mvs) - 1)

            indices[i] = mv_idx
            choices[i] = mvs[str(mv_idx)]
            # print(choices[i])

        return self.format_object(choices)

    def generate_save_one_drop_one(self, data, k=10):
        gender = random.randint(0,1)

        mv_list = data[gender]

        first_mv_i = random.randint(0, len(mv_list))
        first_mv = mv_list[str(first_mv_i)]
        u_gender = ''
        if gender == 0: u_gender = 'bg'
        else: u_gender = 'gg'
        rec = mvr(u_gender, first_mv['Song Name'])
        rec_mvs = rec.compute_top_k_similar_mvs(k)

        second_mv_i = random.randint(1, len(rec_mvs) - 1)
        second_mv = rec_mvs[second_mv_i]

        return self.format_object([first_mv, second_mv])




sodogen = SODOGenerator()
data = sodogen.fetch_all_mvs()
# print(sodogen.generate_save_one_drop_one(data))
