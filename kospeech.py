from flask_restx import Resource, Namespace, fields

recognition_api = Namespace(
    "Recogintion", description='AI Kospeech', path="/api/kospeech")


@recognition_api.route('/')
class Recogintion(Resource):

    @recognition_api.response(200, 'Success')
    def get(self):
        return 'Voice Recognition!'
