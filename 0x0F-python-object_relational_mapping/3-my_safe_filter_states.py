#!/usr/bin/python3
"""
script that is safe from SQL injections
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cr = db.cursor()
    check = (argv[4], )
    cr.execute("SELECT * FROM states WHERE name = %s\
    ORDER BY states.id ASC", check)
    lst = cr.fetchall()
    for r in lst:
        print(r)
    cr.close()
    db.close()
