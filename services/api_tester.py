import requests
import time
from database.db import get_db_connection
import uuid

def test_api_service(data):

    url = data["url"]
    method = data.get("method", "GET").upper()
    headers = data.get("headers", {})
    params = data.get("params", {})
    body = data.get("body", {})
    auth = data.get("auth", None)
    timeout = data.get("timeout", 10)

    try:

        start = time.time()

        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=body,
            auth=auth,
            timeout=timeout
        )

        end = time.time()

        latency = (end - start) * 1000

        try:
            response_body = response.json()
        except:
            response_body = response.text

        conn = get_db_connection()

        cursor = conn.cursor()
        random_id = str(uuid.uuid4())

        cursor.execute("""
            INSERT INTO requests(id,url,method,status_code,latency,response_size) VALUES (%s,%s,%s,%s,%s,%s)
        """,(random_id,url,method,response.status_code,latency,len(response.content)))
        conn.commit()
        conn.close()
        return {
            "status_code": response.status_code,
            "latency_ms": latency,
            "response_size": len(response.content),
            "headers": dict(response.headers),
            "body": response_body
        }

    except Exception as e:

        return {
            "error": str(e)
        }