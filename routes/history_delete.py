from flask import Blueprint,request,jsonify
from services.history_delete import delete_history_request
from services.history_delete import delete_load_request_history

history_delete_simple_bp = Blueprint("history_delete_simple_bp",__name__)
history_delete_load_bp = Blueprint("history_delete_load_bp",__name__)


@history_delete_simple_bp.route("/api/history/<id>",methods=["DELETE"])
def delete_history(id):
    return jsonify(delete_history_request(id))


@history_delete_load_bp.route("/api/history_load_test/<id>",methods=["DELETE"])
def delete_load_history(id):
    return jsonify(delete_load_request_history(id))
