#!/usr/bin/python3
'''Query with MySQLdb'''


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    my_query = "SELECT cities.name FROM cities " \
               "LEFT JOIN states ON states.id = cities.state_id " \
               "WHERE states.name = %s ORDER BY cities.id ASC;"
    cur.execute(my_query, (argv[4],))
    query_rows = cur.fetchall()
    cities = []
    for row in query_rows:
        cities.append(row[0])
    print(", ".join(cities))
    cur.close()
    db.close()
