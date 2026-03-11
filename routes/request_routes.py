from flask import Blueprint, request, jsonify
from services.api_tester import test_api_service

request_bp = Blueprint("request_bp", __name__)

@request_bp.route("/api/request", methods=["POST"])
def test_api():

    data = request.json

    result = test_api_service(data)

    return jsonify(result)