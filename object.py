from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required
import mysql.connector
import jwt

class TaApp:
    def __init__(self, db_config, jwt_secret_key):
        self.app = Flask(__name__)
        self.db = mysql.connector.connect(**db_config)
        self.jwt = JWTManager(self.app)
        self.app.config['JWT_SECRET_KEY'] = jwt_secret_key
        self.cursor = self.db.cursor()

    def run(self):
        self.app.run(debug=True)

    def close_db_connection(self):
        self.db.close()

    def encode_jwt_token(self, payload):
        secret_key = self.app.config['JWT_SECRET_KEY']
        jwt_token = jwt.encode(payload, secret_key, algorithm='HS256')
        return jwt_token

    @staticmethod
    def build_ta_dict(result):
        return {
            'id': result[0],
            'native_english_speaker': bool(result[1]),
            'course_instructor': result[2],
            'course': result[3],
            'semester': bool(result[4]),
            'class_size': result[5],
            'class_attribute': result[6]
        }

    @jwt_required()
    def create_ta(self):
        data = request.get_json()
        query = "INSERT INTO TA (native_english_speaker, course_instructor, course, semester, class_size, class_attribute) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (
            int(data['native_english_speaker']),
            data['course_instructor'],
            data['course'],
            int(data['semester']),
            data['class_size'],
            data['class_attribute']
        )
        self.cursor.execute(query, values)
        self.db.commit()
        return jsonify({'message': 'TA created successfully'}), 201

    @jwt_required()
    def retrieve_ta(self, id):
        query = "SELECT * FROM TA WHERE id = %s"
        self.cursor.execute(query, (id,))
        result = self.cursor.fetchone()
        if result:
            ta = self.build_ta_dict(result)
            return jsonify(ta)
        return jsonify({'error': 'TA not found'}), 404

    @jwt_required()
    def update_ta(self, id):
        data = request.get_json()
        query = "UPDATE TA SET native_english_speaker = %s, course_instructor = %s, course = %s, semester = %s, class_size = %s, class_attribute = %s WHERE id = %s"
        values = (
            int(data['native_english_speaker']),
            data['course_instructor'],
            data['course'],
            int(data['semester']),
            data['class_size'],
            data['class_attribute'],
            id
        )
        self.cursor.execute(query, values)
        self.db.commit()
        return jsonify({'message': 'TA updated successfully'})

    @jwt_required()
    def delete_ta(self, id):
        self.cursor.execute('DELETE FROM TA WHERE id = %s', (id,))
        self.db.commit()
        return jsonify({'message': 'TA deleted successfully'})

    def register_routes(self):
        self.app.route('/ta', methods=['POST'])(self.create_ta)
        self.app.route('/ta/<int:id>', methods=['GET'])(self.retrieve_ta)
        self.app.route('/ta/<int:id>', methods=['PUT'])(self.update_ta)
        self.app.route('/ta/<int:id>', methods=['DELETE'])(self.delete_ta)

if __name__ == '__main__':
    db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'ta_db'
    }
    jwt_secret_key = 'my_secret_key'

    app = TaApp(db_config, jwt_secret_key)
    app.register_routes()
    app.run()
