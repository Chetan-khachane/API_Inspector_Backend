from flask import Flask
from routes.request_routes import request_bp
from routes.loadtest_routes import load_test_bp
from routes.history_routes import history_bp
from routes.history_delete import history_delete_simple_bp
from routes.history_delete import history_delete_load_bp
from flask_cors import CORS
from database.db import get_db_connection

conn = get_db_connection()
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS requests (
        id uuid PRIMARY KEY,
        url TEXT,
        method TEXT,
        status_code INT,
        latency FLOAT,
        response_size INT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

cur.execute("""
    CREATE TABLE IF NOT EXISTS load_tests(
        id uuid PRIMARY KEY,
        url TEXT,
        total_request INT,
        concurrency INT,
        avg_latency FLOAT,
        min_latency FLOAT,
        max_latency FLOAT,
        success_rate FLOAT,
        error_rate FLOAT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

conn.commit()
conn.close()


app = Flask(__name__)
CORS(app)

app.register_blueprint(request_bp)
app.register_blueprint(load_test_bp)
app.register_blueprint(history_bp)
app.register_blueprint(history_delete_simple_bp)
app.register_blueprint(history_delete_load_bp)

# POST /api/request
# POST /api/load-test
# GET  /api/history
# DELETE /api/history/<id>
# GET  /api/analytics
# POST /api/ai-analysis


if __name__ == "__main__":
    port = 7860
    app.run(host="0.0.0.0", port=port)

