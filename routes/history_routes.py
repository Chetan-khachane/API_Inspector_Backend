from flask import Blueprint,request,jsonify
from services.history import find_history
history_bp = Blueprint("history_bp",__name__)

@history_bp.route("/api/history",methods=["GET"])
def get_history():
    result = find_history()

    return jsonify(result)