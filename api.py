from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required
import mysql.connector
import jwt
app = Flask(__name__)
import secrets


secret_key ='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMjM0LCJzdWIiOiJ1c2VyMTIzIiwidXNlcm5hbWUiOiJqb2huX2RvZSJ9.wVOQ1tVBVOx8AVp4f-o8iF5ZwmzsBPwAdounWocz8Jk'
app.config['JWT_SECRET_KEY'] = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMjM0LCJzdWIiOiJ1c2VyMTIzIiwidXNlcm5hbWUiOiJqb2huX2RvZSJ9.wVOQ1tVBVOx8AVp4f-o8iF5ZwmzsBPwAdounWocz8Jk'
payload = {'user_id': 1234,"sub": "user123", 'username': 'john_doe'}
jwt_token = jwt.encode(payload, secret_key, algorithm='HS256')
print(jwt_token)
jwt = JWTManager(app)


db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='ta_db'
)
cursor = db.cursor()


@app.route('/ta', methods=['POST'])
@jwt_required()
def create_ta():    
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
    cursor.execute(query, values)
    db.commit()
    return jsonify({'message': 'TA created successfully'}), 201


@app.route('/ta/<int:id>', methods=['GET'])
@jwt_required()
def retrieve_ta(id):    
    query = "SELECT * FROM TA WHERE id = %s"
    cursor.execute(query, (id,))
    result = cursor.fetchone()    
    if result:
        ta = {
            'id': result[0],
            'native_english_speaker': bool(result[1]),
            'course_instructor': result[2],
            'course': result[3],
            'semester': bool(result[4]),
            'class_size': result[5],
            'class_attribute': result[6]
        }
        return jsonify(ta)    
    return jsonify({'error': 'TA not found'}), 404


@app.route('/ta/<int:id>', methods=['PUT'])
@jwt_required()
def update_ta(id):  
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
    cursor.execute(query, values)
    db.commit()    
    return jsonify({'message': 'TA updated successfully'})


@app.route('/ta/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_ta(id):    
    cursor.execute('DELETE FROM TA WHERE id = %s', (id,))
    db.commit()  
    return jsonify({'message': 'TA deleted successfully'})


if __name__ == "__main__":
    app.run(debug=True)


