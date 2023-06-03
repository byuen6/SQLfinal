import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="password",  # your password
                     db="menagerie")        # name of the data base


cur = db.cursor()

cur.execute("DROP DATABASE IF EXISTS menagerie")
for row in cur.fetchall():
    print (row)

db.close()