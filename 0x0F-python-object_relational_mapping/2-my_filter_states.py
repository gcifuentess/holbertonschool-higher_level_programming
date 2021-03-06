#!/usr/bin/python3
'''Query with MySQLdb'''


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    my_query = "SELECT * FROM states " \
               "WHERE name = '{}' ORDER BY states.id ASC"
    fmt_query = my_query.format(argv[4])
    cur.execute(fmt_query)
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == argv[4]:
            print(row)
    cur.close()
    db.close()
