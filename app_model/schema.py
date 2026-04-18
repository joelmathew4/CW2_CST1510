def create_user_table(conn):
    cur = conn.cursor()
    sql = ''' CREATE TABLEusers ()
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL):
    '''
    cur.execute(sql)
    conn.commit()