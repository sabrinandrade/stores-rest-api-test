from models.user import UserModel
from flask_restful import Resource, reqparse


class UserRegister(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank.")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank.")

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message':  'User already exists on the database'}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {'message':  'User created successfully'}, 201
