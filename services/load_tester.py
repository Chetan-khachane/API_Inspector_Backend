from concurrent.futures import ThreadPoolExecutor
from flask import jsonify
import requests
import time
from utils.metrics import calculate_performance
from database.db import get_db_connection
import uuid


latencies = []

def send_request(req):
    try:
        start = time.time()
        response = requests.request(
            method=req["method"],
            url=req["url"],
            headers=req["headers"],
            params=req["params"],
            json=req["body"],
            auth=req["auth"],
            timeout=req["timeout"]
        )
        end = time.time()

        latency = (end - start) * 1000
        
        

        return {
            "latency" : latency,
            "success" : response.status_code < 400
        }
    except Exception:

        return {
            "latency": None,
            "success": False
        }

def load_test(data):

    url = data["url"]
    method = data.get("method", "GET").upper()
    headers = data.get("headers", {})
    params = data.get("params", {})
    body = data.get("body", {})
    auth = data.get("auth", None)
    timeout = data.get("timeout", 10)

    concurrency = data.get("concurrency", 10)
    requests_count = data.get("requests_count", 50)

    req = {
        "url" : url,
        "method" : method,
        "headers" : headers,
        "params" : params,
        "body" : body,
        "auth" : auth,
        "timeout" : timeout
    }

 

    global latencies
    final_performace = dict()
    success_count = 0
    failure_count = 0
    with ThreadPoolExecutor(max_workers=concurrency) as executor:

        results = list(executor.map(send_request,[req]*requests_count))
        latencies = [r["latency"] for r in results if r["latency"] is not None]
        success_count = sum(1 for r in results if r["success"])
        failure_count = requests_count - success_count
        
    final_performace = calculate_performance(latencies,success_count,failure_count,requests_count)

    conn = get_db_connection()
    cursor = conn.cursor()
    random_id = str(uuid.uuid4())
    cursor.execute("""
            INSERT INTO load_tests(id,url,total_request,concurrency,avg_latency,min_latency,max_latency,success_rate,error_rate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """,(random_id,url,requests_count,concurrency,final_performace.get("avg_latency"),
             final_performace.get("min_latency"),final_performace.get("max_latency"),
             final_performace.get("success_rate"),
             final_performace.get("error_rate")
             ))
    conn.commit()
    conn.close()
    return final_performace