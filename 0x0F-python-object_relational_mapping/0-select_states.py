#!/usr/bin/python3
"""
list states from db hbtn_0e_usa
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states ORDER BY states.id ASC""")
    lst = cur.fetchall()
    for r in lst:
        print(r)
    cur.close()
    db.close()
