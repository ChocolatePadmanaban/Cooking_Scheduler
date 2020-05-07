# https://pymotw.com/3/sqlite3/index.html
# refer the above site for detailed explaination

import os
import sqlite3

def createdb(db_filename='todo.db'):
    
    db_is_new = not os.path.exists(db_filename)
    conn = sqlite3.connect(db_filename)

    if db_is_new:
        print('Need to create schema')
    else:
        print('Database exists , assume schemadoes, too.')

    conn.close()

if __name__ == "__main__":
    createdb()