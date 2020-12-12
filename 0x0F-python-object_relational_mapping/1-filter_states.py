#!/usr/bin/python3
'''Query with MySQLdb'''


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("\
    SELECT * FROM states WHERE states.name REGEXP '^N' \
    ORDER BY states.id ASC;")
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1][0] == 'N':
            print(row)
    cur.close()
    db.close()
