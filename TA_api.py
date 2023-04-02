# from secrets_key import secret_key
from flask import Flask, jsonify, request
import mysql.connector
import jwt
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)

# Generate a key for Headers( Auth : Bearer )


app.config['JWT_SECRET_KEY'] = 'my-secret-key'

jwt = JWTManager(app)


### MySQL data base configuration #######
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='ta_db'
)
cursor = db.cursor()

##################### Login AUTH user ###############


def generate_token(user_id, username):
    token = create_access_token(identity=user_id)
    return token

# Login route


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    # check if user exists in the database and return JWT token
    query = "SELECT id, username, password FROM users WHERE username = %s AND password = %s"
    values = (username, password)
    cursor.execute(query, values)
    user = cursor.fetchone()

    if user:
        user_id = user[0]
        token = generate_token(user_id=user_id, username=username)
        return jsonify([{"Welcome": username.title(), "Your access_token is": token}]), 200

    return jsonify({"msg": "Invalid username or password"}), 401


def create_user(username, password):
    cursor = db.cursor()
    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    cursor.execute(query, (username, password))
    db.commit()


@app.route('/signup', methods=['POST'])
def signup():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    # create a new user in the database
    create_user(username, password)
    # return a success message
    return jsonify({"msg": "User created successfully"}), 201


@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


@app.route("/users")
def user():
    quiry = "select * from users"
    cursor.execute(quiry)
    result = cursor.fetchall()
    return jsonify({"users": result})


################ CRUD #################


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


@app.route('/ta', methods=['POST'])
@jwt_required()
def create_ta():
    data = request.get_json()
    query = "INSERT INTO TA (class_attribute, class_size, course, course_instructor, native_english_speaker, semester) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (
        int(data['class_attribute']),
        int(data['class_size']),
        data['course'],
        data['course_instructor'],
        bool(data['native_english_speaker']),
        bool(data['semester'])
    )

    cursor.execute(query, values)
    db.commit()
    return jsonify({'message': 'TA created successfully'})


@app.route('/ta', methods=['GET'])
def get_all_ta():
    cursor.execute('SELECT * FROM TA')
    result = cursor.fetchall()

    if result:
        ta_list = []
        for row in result:
            ta_dict = {
                'id': row[0],
                'course': row[3],
                'class_size': row[1],
                'semester': bool(row[5]),
                'course_instructor': row[2],
                'native_english_speaker': bool(row[4]),
                'class_attribute': row[6]
            }
            ta_list.append(ta_dict)

        return jsonify({"data": ta_list}), 200
    return jsonify({"message": "Data not found in database"}), 404


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


@app.route('/ta', methods=['DELETE'])
@jwt_required()
def delete_all_ta():
    cursor.execute('DELETE FROM TA')
    db.commit()
    return jsonify({'message': 'All TA data deleted successfully'})


if __name__ == "__main__":
    app.run(debug=True)
