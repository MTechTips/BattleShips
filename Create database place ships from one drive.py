import sqlite3


connection = sqlite3.connect("ships.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE ships(position,afloat)")