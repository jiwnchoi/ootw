from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
from flask import jsonify
from pymongo import MongoClient


client = MongoClient('localhost',27017)

db = client["ootw"]
collection = db["user"]
print(collection.find_one())

app = Flask(__name__)
api = Api(app)
class SignUp(Resource):
    def post(self):
         
        return 1

class SignIn(Resource):
    def post(self):
        return 1

class AddData(Resource):
    def post(self):
        return 1

class GetData(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str)
        parser.add_argument('date', type=int, action="append")
        parser.add_argument('data', type=int)
        args = parser.parse_args()
        return 1

class UpdateData(Resource):
    def post(self):
        return 1
 
api.add_resource(SignUp, '/signup')
api.add_resource(SignIn, '/signin')

api.add_resource(AddData, '/add')
api.add_resource(GetData, '/get')
api.add_resource(UpdateData, '/update')

 
if __name__ == '__main__':
    app.run(debug=True)