import sqlite3

def updateTable(Name, Price, Wins):
    sql_update_query = "Update decks SET Price = ?, Wins = ? where Short = ?"
    data = (Price, Wins, Name)
    cur.execute(sql_update_query,data)

db = sqlite3.connect('DatabaseCQ.db')
cur = db.cursor()
cur.execute('DROP TABLE IF EXISTS decks')
cur.execute('CREATE TABLE decks (Short text, Colors text, FullName text, Price real, Wins int)')
cur.execute("INSERT INTO decks VALUES ('Arix','UG','Arixmethes, the Slumbering Isle',450.28,5)")
for row in cur.execute('SELECT * FROM decks'):
    print(row)

addColumn = "ALTER TABLE decks ADD COLUMN Address text"
cur.execute(addColumn)
for row in cur.execute('SELECT * FROM decks'):
    print(row)

cur.execute("CREATE TABLE decks_backup AS SELECT Short, Colors, FullName, Price, Wins FROM decks")
cur.execute("DROP TABLE decks")
cur.execute("ALTER TABLE decks_backup RENAME TO decks")


cur.execute("INSERT INTO decks VALUES ('Ur-Dragon','WUBRG','The Ur-Dragon',1347.29,30)")
cur.execute("INSERT INTO decks VALUES ('Aegar','UR','Aegar, the Freezing FLame',160.34,2)")
for row in cur.execute('SELECT * FROM decks'):
    print(row)

cur.execute('SELECT * FROM decks')
rows = cur.fetchall()
for row in rows:
    print(row)

updateTable('Aegar',209.5,4)
for row in cur.execute('SELECT * FROM decks'):
    print(row)
    
db.commit()
db.close()