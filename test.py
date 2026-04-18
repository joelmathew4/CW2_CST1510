import bcrypt
import os
import sqlite3
def hash_password(plain_text_password):
    password_bytes = plain_text_password.encode("utf-8")

    salt = bcrypt.gensalt()
    bcrypted_password = bcrypt.hashpw(password_bytes, salt )
    return(bcrypted_password.decode('utf-8'))


def verify_password(plain_text_password, hash_password_):
    password_bytes = plain_text_password.encode("utf-8")
    hash_password_bytes = hash_password_.encode("utf-8")
    if bcrypt.checkpw(password_bytes, hash_password_bytes):
        print('Password is correct')
    else:
        print("password is incorrect")


def register_user():
    user_name=input('what is your name?')
    password=input('what is your password?')
    h_password=hash_password(password)
    with open ('DATA/users.text','a')as f:
        f.write(f"{user_name},{h_password}\n")
        print('User registered successfully!')
    
def login_user():
    user_name=input('what is your name?')
    password=input('what is your password?')
    h_password=hash_password(password)
    with open ('DATA/users.text','r')as f:
        users=f.readlines()
    for user in users:
        stored_user_name, stored_h_password = user.strip().split(',')
        if stored_user_name==user_name:
            verify_password(password,stored_h_password)
            return
    return False

def main():
    while True:
            print('welcome to user authentication system!')
            print("1. Register")
            print('2. Login')
            print('3. Exit')
            choice=input('Please enter your choice(1,2,or 3):')
            if choice=='1':
                register_user()
            elif choice=='2':
                login_user()
            elif choice=='3':
                print('Goodbye!')
                break
            else:
                print('Invalid choice. Please try again')


def create_user_table(conn):
   cursor = conn.cursor()
   sql = """ CREATE TABLE IF NOT EXISTS users ( id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT NOT NULL UNIQUE, password_hash TEXT NOT NULL)"""
   cursor.execute(sql)
   conn.commit()

def add_user(conn, username, password_hash):
    conn = sqlite3.connect('DATA/intelligent_platporm.db')

    cursor = conn.cursor()
    sql = """INSERT INTO users (username, password_hash) VALUES (?, ?)"""
    param = ('Joel','dfghjhjgtvb')
    cursor.execute(sql, param)
    conn.commit()
    conn.close()


def migrate_users_to_db():
    conn = sqlite3.connect('DATA/intelligent_platporm.db')
    with open('DATA/user.txt','r') as f:
        users = f.readlines()
    for user in users:
        stored_user_name, stored_h_password = user.strip().split(',')
        add_user(conn, stored_user_name, stored_h_password)
    print("Users migrated to database successfully!")
    conn.close()


def create_user_table(conn):
    cur=conn.cursor()
    sql='''CREATE TABLE users ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    username TEXT NOT NULL UNIQUE, 
    password_hash TEXT NOT NULL );'''  
    cur.execute(sql)
    conn.commit()



conn = sqlite3.connect('DATA/intelligent_platporm.db')
cur=conn.cursor()
sql='''INSERT INTO users (username, password_hash) VALUES (?, ?) '''
param= ('Joel','dfghjhjgtvb')
cur.execute(sql, param)
conn.commit()

conn.close()

