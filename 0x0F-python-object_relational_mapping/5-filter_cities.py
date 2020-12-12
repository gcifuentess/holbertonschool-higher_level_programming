#!/usr/bin/python3
'''Query with MySQLdb'''


if __name__ == "__main__":
    import MySQLdb
    import sys

    argv = sys.argv
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    my_query = "SELECT cities.name FROM cities " \
               "LEFT JOIN states ON states.id = cities.state_id " \
               "WHERE states.name = %s ORDER BY cities.id;"
    cur.execute(my_query, (argv[4],))
    query_rows = cur.fetchall()
    for row in query_rows:
        for col in row:
            if row != query_rows[-1]:
                print("%s" % col, end=", ")
            else:
                print(col)
    cur.close()
    db.close()
