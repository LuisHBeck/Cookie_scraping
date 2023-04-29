from connect import cursor

def read_draw(x):
    sql = f'SELECT * from {x}'

    cursor.execute(sql)
    result = cursor.fetchall()

    return result