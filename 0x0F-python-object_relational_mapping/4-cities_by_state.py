#!/usr/bin/python3
'''Query with MySQLdb'''


if __name__ == "__main__":
    import MySQLdb
    import sys

    argv = sys.argv
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    my_query = "SELECT cities.id, cities.name, states.name FROM " \
               "cities LEFT JOIN states ON states.id = cities.state_id " \
               "ORDER BY cities.id;"
    cur.execute(my_query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
