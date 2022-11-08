from flask import Flask
from flask_cors import CORS
from flask_restx import Api
from kospeech import recognition_api


def create_app(test_config=None):
    app = Flask(__name__)

    api = Api(app, version='1.0', title='ASAP API 문서',
              description='ML', doc="/api-docs")
    api.add_namespace(recognition_api)

    CORS(app, resources={r'/api/*': {'origins': '*'}})

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
