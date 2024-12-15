from django.db import connection

def calculate_fine(due_date, returned_date):
    """
    Calls the PostgreSQL calculate_fine function.
    """
    with connection.cursor() as cursor:
        cursor.execute("SELECT calculate_fine(%s, %s)", [due_date, returned_date])
        result = cursor.fetchone()
    if result is None:
        return None  # Or handle it in another way if needed
    return result[0]

def get_user_borrowed_books(user_id):
    """
    Calls the PostgreSQL get_user_borrowed_books function.
    """
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM get_user_borrowed_books(%s)", [user_id])
        if cursor.description is None:  # No columns returned
            return []  # Or handle it appropriately
        columns = [col[0] for col in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return results