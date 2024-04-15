from flask import make_response, jsonify


class Errors:

    @staticmethod
    def register_errors(app):
        @app.errorhandler(404)
        def not_found_error(error):
            return make_response(jsonify({'error': 'Not found'}), 404)

        @app.errorhandler(500)
        def internal_server_error(error):
            return make_response(jsonify({'error': 'Internal Server Error'}), 500)

        @app.errorhandler(400)
        def bad_request(error):
            return make_response(jsonify({'error': 'Bad Request'}), 400)
