import bcrypt
import os
import sqlite3
import pandas as pd
from app_model.db import conn 
from app_model.db import add_user , get_user





def register_user(conn):
    name=input('Enter your name: > ')
    password=input('Enter your password: > ')
    hash_password = generate_hash(password)
    add_user(conn, name, hash_password)
   
    
def log_in_user(conn):
    name=input('what is your name?')
    password=input('what is your password?')
    id,user_name, user_hash = get_user(conn,name)
    print(f'Welcome{user_name}!!')
    if name==user_name and is_valid_hash(password,user_hash):
            return True
    return False

def main():
    while True:
            print('Welcome to thesystem!')
            print('Choose from the following options:')
            print("1. To Register")
            print('2. To Login')
            print('3. To Exit')
            choice=input(':>')
            if choice=='1':
                register_user(conn)
            elif choice=='2':
                if log_in_user(conn):
                    print('Login successful!')
                else:
                    print('Invalid credentials.')
            elif choice=='3':
                print('Goodbye!')
                break
            else:
                print('Invalid choice. Please try again')


if __name__ == "__main__":  
    main()