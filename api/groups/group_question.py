from flask_restful import Api, Resource, request, abort, fields, marshal_with, reqparse
from groups.question_generator import GroupQuestionGenerator as GGQ

q_gen = GGQ()

from firebase_admin import auth


class GroupQuestion(Resource):
    def get(self, gender, type):
        # return str(gender) + ' ' + str(type)

        id_token = request.headers['Authorization']
        # id_token comes from the client app (shown above)
        try:
            decoded_token = auth.verify_id_token(id_token)
            uid = decoded_token['uid']
            data = q_gen.fetch_all_groups(gender)
            result = {}
            if type == "debut":
                result = q_gen.debut_q(data)
            elif type == "c-members":
                result = q_gen.current_members_q(data)
            elif type == "o-members":
                result = q_gen.original_members_q(data)
            elif type == "fandom":
                result = q_gen.fandom_name_q(data)
            elif type == "korean":
                result = q_gen.korean_name_q(data)
            elif type == "company":
                result = q_gen.company_q(data)
            elif type == "allgroups":
                result = data
            if not result:
                abort(404, message="Wrong gender or type of question")

            return result, 201
        except:
            abort(404, message="ID invalid")

        
