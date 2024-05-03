from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Users(Resource):
    def get(self, cpf):
        return {'cpf': cpf}


api.add_resource(Users, '/users/<string:cpf>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
