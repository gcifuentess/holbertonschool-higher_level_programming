#!/usr/bin/python3
'''Query with MySQLdb'''
import MySQLdb
import sys


argv = sys.argv
db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2],
                     db=argv[3], charset="utf8")
cur = db.cursor()
cur.execute("SELECT * FROM states WHERE name REGEXP '^N' ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
db.close()
