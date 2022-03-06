from flask import request
from flask_restful import Api, Resource, abort
from mvs.save_one_drop_one_generator import SODOGenerator as SODO

sodo_gen = SODO()

from firebase_admin import auth

class SODOQuestion(Resource):
    def get(self):
        id_token = request.headers['Authorization']
        # id_token comes from the client app (shown above)
        try:
            decoded_token = auth.verify_id_token(id_token)
            uid = decoded_token['uid']

            data = sodo_gen.fetch_all_mvs()
            # result = sodo_gen.generate_sodo(data)
            result = sodo_gen.generate_save_one_drop_one(data, 3)

            if not result:
                abort(404, message="Wrong query")
            return result, 201
        except Exception as e:
            print(e)
            abort(401, message="ID not valid")

        # data = sodo_gen.fetch_all_mvs()
        # result = sodo_gen.generate_save_one_drop_one(data)
        # print(id_token)
        # if not result:
        #     abort(404, message="Wrong query")
        # return result, 201


