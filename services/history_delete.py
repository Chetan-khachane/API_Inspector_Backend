from database.db import get_db_connection

def delete_history_request(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
            DELETE FROM requests WHERE id=%s
    """,(id,))
    conn.commit()
    conn.close()
    return {
        "id"  : id,
        "status" : "Successfully deleted"
    }


def delete_load_request_history(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
            DELETE FROM load_tests WHERE id=%s
    """,(id,))
    conn.commit()
    conn.close()
    return {
        "id"  : id,
        "status" : "Successfully deleted"
    }
