#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(user='root',
                               passwd='',
                               db='hbtn_0e_0_usa')
    curs = database.cursor()
    curs.execute("SELECT * FROM states WHERE\
                  name LIKE BINARY '{}'\
                  ORDER BY states.id ASC".format(argv[4]))
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    database.close()
