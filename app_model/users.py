
from app_model.db import get_connection


def add_user(username: str, password_hash: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users (username, password_hash)
        VALUES (?, ?)
    """, (username, password_hash))

    conn.commit()
    conn.close()



def get_user(username: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, username, password_hash
        FROM users
        WHERE username = ?
    """, (username,))

    user = cursor.fetchone()
    conn.close()

    return user



def get_all_users(conn):
    cur=conn.cursor()
    sql='''SELECT * FROM users'''
    cur.execute(sql)
    users=cur.fetchall()

    return (users)  



def get_user(conn, name):
    cur=conn.cursor()
    sql='''SELECT * FROM users WHERE username=?'''
    param=(name,)
    cur.execute(sql,param)
    return cur.fetchone()




def update_user(conn, old_name, new_name):
    cur=conn.cursor()
    sql='UPDATE users SET username= ? WHERE username=?'
    param=(new_name, old_name)
    cur.execute(sql,param)
    conn.commit()


def delete_user(conn, user_name):
    cur=conn.cursor()
    sql='''DELETE FROM users WHERE username=?'''
    param=(user_name,)
    cur.execute(sql,param)
    conn.commit()

    from app_model.db import get_connection



def add_user(username: str, password_hash: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users (username, password_hash)
        VALUES (?, ?)
    """, (username, password_hash))

    conn.commit()
    conn.close()



def get_user(username: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, username, password_hash
        FROM users
        WHERE username = ?
    """, (username,))

    user = cursor.fetchone()
    conn.close()

    return user
