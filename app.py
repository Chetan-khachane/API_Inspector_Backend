from flask import Flask
from routes.request_routes import request_bp
from routes.loadtest_routes import load_test_bp
from routes.history_routes import history_bp
from routes.history_delete import history_delete_simple_bp
from routes.history_delete import history_delete_load_bp
from flask_cors import CORS



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
    app.run(debug=True)

