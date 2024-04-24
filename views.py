from flask import request, jsonify, g
from .database import get_db, close_db
from .serializers import SubmitDataSerializer

def submit_data():
    try:
        data = request.get_json()
        coordinates = data.get('coordinates')
        height = data.get('height')
        name = data.get('name')
        photos = data.get('photos')
        user_name = data.get('user_name')
        email = data.get('email')
        phone = data.get('phone')

        if not all([coordinates, height, name, user_name, email, phone]):
            return jsonify({'success': False, 'error': 'Missing required fields'}), 400

        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
            INSERT INTO mountain_passes (coordinates, height, name, photos, user_name, email, phone)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (coordinates, height, name, photos, user_name, email, phone))
        db.commit()

        return jsonify({'success': True}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
