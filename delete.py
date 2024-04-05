# -*- coding: utf-8 -*-
# @Author: Dastan_Alam
# @Date:   23-03-2024 11:11:30 PM       23:11:30
# @Last Modified by:   Dastan_Alam
# @Last Modified time: 23-03-2024 11:11:55 PM       23:11:55
import sqlite3

def clean_table(table_name):
    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute(f'DELETE FROM {table_name}')
        conn.commit()
        print(f'All data deleted from table {table_name}')
    except sqlite3.Error as e:
        print(f'An error occurred: {e}')
    finally:
        conn.close()

# Usage
if __name__ == '__main__':
    table_name = 'users'  # Specify the table name you want to clean
    clean_table(table_name)