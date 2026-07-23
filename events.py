from flask import Blueprint, jsonify, request
from db import get_db_connection

events_bp = Blueprint('events', __name__, url_prefix='/api/events')

# 取得
@events_bp.route('', methods=['GET'])
def get_events():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    sql = "SELECT id, user_id, title, start_time, end_time FROM events"
    cursor.execute(sql)
    events = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return jsonify(events), 200

# 追加
@events_bp.route('', methods=['POST'])
def create_events():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    
    sql = "INSERT INTO events (user_id, title, start_time, end_time) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (1, data['title'], data['start_time'], data['end_time']))
    
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Event created successfully"}), 201

# 更新
@events_bp.route('/<int:event_id>', methods=['PUT'])
def update_events(event_id):
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = "UPDATE events SET title = %s, start_time = %s, end_time = %s WHERE id = %s"
    cursor.execute(sql, (data['title'], data['start_time'], data['end_time'], event_id))
    
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Event updated successfully"}), 200

# 削除
@events_bp.route('/<int:event_id>', methods=['DELETE'])
def delete_events(event_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = 'DELETE FROM events WHERE id = %s'
    cursor.execute(sql, (event_id))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Event deleted successfully"}), 200
