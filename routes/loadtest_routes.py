from flask import Blueprint,request,jsonify
from services.load_tester import load_test
load_test_bp = Blueprint("load_test_bp",__name__)

@load_test_bp.route("/api/load_test",methods=["POST"])
def load_test_api():
    data = request.json
    result = load_test(data)
    return jsonify(result)