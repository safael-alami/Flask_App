import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd=""
)


cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS flaskdb;")
db.close()

print("Base de données créée avec succès.")
