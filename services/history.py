from database.db import get_db_connection
def find_history():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(""" 
        SELECT * FROM requests 
        ORDER BY created_at DESC
    """)


    simple_rows = cursor.fetchall()

    cursor.execute("""
        SELECT * FROM load_tests ORDER BY created_at DESC
""")
    
    load_test_rows = cursor.fetchall()
    cursor.close()
    conn.close()
    
    simple_request_history = []
    load_test_history = []

    for row in simple_rows:
        simple_request_history.append({
            "id": row[0],
            "url": row[1],
            "method": row[2],
            "status_code": row[3],
            "latency": row[4],
            "response_size": row[5],
            "created_at": row[6]
        })
    
    for row in load_test_rows:
        load_test_history.append({
            "id" : row[0],
            "url" : row[1],
            "total_request" : row[2],
            "concurrency" : row[3],
            "avg_latency" : row[4],
            "min_latency" : row[5],
            "max_latency" : row[6],
            "success_rate" : row[7],
            "error_rate" : row[8],
            "created_at" : row[9]
        })

    return {
        "simple_test" : simple_request_history,
        "load_test" : load_test_history
    }