from flask import Flask, request, jsonify
from config import DATABASE
from database import Database

app = Flask(__name__)
db = Database(**DATABASE)

@app.route('/submitData', methods=['POST'])
def submit_data():
    data = request.get_json()
    coordinates = data.get('coordinates')
    height = data.get('height')
    name = data.get('name')
    photos = data.get('photos')
    user_name = data.get('user_name')
    email = data.get('email')
    phone = data.get('phone')

    db.submit_data(coordinates, height, name, photos, user_name, email, phone)

    return jsonify({'success': True}), 200

if __name__ == '__main__':
    app.run(debug=True)