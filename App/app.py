from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Food Security App'
#AUTHENTICATION AND WHAT NOT
#signing up

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username and password:
        insert_user(username, password)
        return jsonify({'message': 'User created successfully'}), 201
    else:
        return jsonify({'message': 'Username and password are required'}), 400

@app.route('/signin', methods=['POST'])
def signin():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username and password:
        user = get_user(username)
        if user and check_password_hash(user['password'], password):
            return jsonify({'message': 'Sign-in successful'}), 200
        else:
            return jsonify({'message': 'Invalid username or password'}), 401
    else:
        return jsonify({'message': 'Username and password are required'}), 400

if __name__ == '__main__':
    app.run(debug=True)