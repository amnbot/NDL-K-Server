from flask_restful import Api, Resource, abort
from idols.question_generator import IdolQuestionGenerator as IG

q_gen = IG()


class IdolQuestion(Resource):
    def get(self, gender, type):

        data = q_gen.fetch_all_idols(gender)
        result = {}

        if type == "birthyear":
            result = q_gen.birthyear_q(data)
        elif type == 'korean-name':
            result = q_gen.korean_name_q(data)
        elif type == 'group':
            result = q_gen.group_q(data)
        if not result:
            abort(404, message="Wrong query")
        return result, 201
