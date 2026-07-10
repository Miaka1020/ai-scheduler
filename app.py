from flask import Flask, jsonify
from db import get_db_connection

app = Flask(__name__)

# 予定の一覧を取得 
@app.route('/api/events', methods=['GET'])
def get_events():
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, title, start_time, end_time FROM events")
            events = cursor.fetchall()
            
            # 日付データをWebで送信できる文字列形式に変換
            for e in events:
                e['start_time'] = e['start_time'].isoformat()
                e['end_time'] = e['end_time'].isoformat()

            return jsonify(events)
    finally:
        conn.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
