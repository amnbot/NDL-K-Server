import os

from flask import Flask, make_response, request, Response
from flask.json import jsonify
from flask_restful import Api
from flask_cors import CORS, cross_origin
from flask_ngrok import run_with_ngrok

from groups.group_question import GroupQuestion
from idols.idol_question import IdolQuestion
from mvs.mv_question import SODOQuestion


import firebase_admin
from firebase_admin import credentials, auth

cred_path = os.environ.get('NDL-K_CREDENTIALS')
cred = credentials.Certificate(cred_path)
"""
The SDK can also be initialized with no parameters. In this case, the SDK uses Google Application Default Credentials. Because default credentials lookup is fully automated in Google environments, with no need to supply environment variables or other configuration, this way of intializing the SDK is strongly recommeneded for applications running on Compute Engine, Kubernetes Engine, App Engine, and Cloud Functions.
"""
# firebase_admin.initialize_app(cred)
default_app = firebase_admin.initialize_app(credential=cred)




app = Flask(__name__)
api = Api(app)
CORS(app)
#run_with_ngrok(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/", methods=['GET'])
@cross_origin()
def helloWorld():
    # id_token comes from the client app (shown above)
    lang = request.args.get('language')
    id_token = request.headers['Authorization']
    decoded_token = auth.verify_id_token(id_token)
    uid = decoded_token['uid']
    response = jsonify(message=str(uid))
    return response


api.add_resource(GroupQuestion, "/groups/<string:gender>/<string:type>")
api.add_resource(IdolQuestion, "/idols/<string:gender>/<string:type>")
api.add_resource(SODOQuestion, "/mvs/sodo/")

if __name__ == "__main__":
    app.run()
