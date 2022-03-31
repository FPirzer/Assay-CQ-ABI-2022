import sqlite3


db = sqlite3.connect("DatabaseStart.db")
cur = db.cursor()
for x in ["Zutaten", "Supermarkt", "Küche", "Rezept", "Rucksack", "Garten"]:
    cur.execute("DROP TABLE IF EXISTS " + x)

cur.execute(
    "CREATE TABLE Zutaten( Name text, Geschmacksrichtung text, Menge int, Preis_pro_Kilo real, Ernteseason text, foreign key (Preis_pro_Kilo) references Supermarkt(Preis_pro_Kilo))"
)
cur.execute(
    "CREATE TABLE Supermarkt(Waren_ID integer primary key autoincrement, Name text, Abteilung text, Menge int, Preis_pro_Kilo real, Lager text)"
)
cur.execute("CREATE TABLE Küche( Name text, Lagerungsart text, Menge int, Platz text)")
cur.execute(
    "CREATE TABLE Rezept( Rezept_ID int, Name text, Kochart text, Kochzeit int, Aufwand text)"
)
cur.execute("CREATE TABLE Rucksack( Name text, Menge int, Gewicht real)")
cur.execute(
    "CREATE TABLE Garten( Name text, Feldnummer int, Menge int, Anbau text, Ernteseason text)"
)

cur.execute("""INSERT INTO Zutaten VALUES("Zwiebel", "Herzhaft", 2, 1.50, "Juli")""")
cur.execute(
    """INSERT INTO Zutaten values ("Kartoffeln", "Herzhaft", 20, 1.90, "August")"""
)
cur.execute(
    """INSERT INTO Zutaten values ("Knoblauch", "Herzhaft", 8, 12.30, "Juni")"""
)
cur.execute("""INSERT INTO Zutaten values ("Tomaten", "Herzhaft", 6, 6.50, "Juli")""")
cur.execute("""INSERT INTO Zutaten Values ("Käse", "Herzhaft", 1, 11.90, "Januar")""")
cur.execute("""INSERT INTO Zutaten Values ("Apfel", "Süß", 6, 5, "Mai")""")
cur.execute("""INSERT INTO Zutaten values ("Birne", "Süß", 2, 3.20, "Mai")""")
cur.execute("""INSERT INTO Zutaten values ("Mango", "Süß", 2, 30, "September")""")
cur.execute("""INSERT INTO Zutaten values ("Banane", "Süß", 7, 7.10, "April")""")
cur.execute("""INSERT INTO Zutaten values ("Traube", "Süß", 1, 4, "Juli")""")


def InsertMarkt(WarenID, Name, Abteilung, Menge, Preis, Lager):
    sql_insert_query = "Insert INTO Supermarkt VALUES(?,?,?,?,?,?)"
    data = (WarenID, Name, Abteilung, Menge, Preis, Lager)
    cur.execute(sql_insert_query, data)


InsertMarkt(None, "Hühnchen", "Fleischtheke", 3, 4.5, "Im Lager")
InsertMarkt(None, "Chips", "Snacks", 12, 1.89, "Im Lager")
InsertMarkt(None, "Gouda", "Käsetheke", 6, 3.5, "Nicht im Lager")
InsertMarkt(None, "Äpfel", "Obstabteilung", 18, 3.6, "Nicht im Lager")
InsertMarkt(None, "Toilettenpapier", "Haushaltswaren", 20, 3.99, "Im Lager")
InsertMarkt(None, "Sonnenblumenöl", "Essig und Öle", 50, 2.99, "Nicht lieferbar")


def InsertGarten(Name, Feldnummer, Menge, Anbau, Ernteseason):
    sql_insert_query = "Insert INTO Garten VALUES(?,?,?,?,?)"
    data = (Name, Feldnummer, Menge, Anbau, Ernteseason)
    cur.execute(sql_insert_query, data)


InsertGarten("Tomaten", 2, 5, "Mai", "August")
InsertGarten("Zwiebeln", 1, 7, "Januar", "Juli")
InsertGarten("Äpfel", 4, 12, "April", "Juni")
InsertGarten("Trauben", 1, 7, "Mai", "Dezember")
InsertGarten("Birnen", 4, 10, "März", "September")
InsertGarten("Schnittlauch", 1, 12, "Oktober", "Februar")


# for row in cur.execute("SELECT * FROM Supermarkt"):
#     print(row)
#
cur.execute("SELECT * FROM Supermarkt")
rows = cur.fetchall()
for row in rows:
    print(row)

# für eine leere Reihe zwischen den Outputs
print()


def updateMarkt(Menge, Preis, Lager, Waren_ID):
    sql_update_query = "Update Supermarkt SET Menge = ?, Preis_pro_Kilo = ? , Lager=? where Waren_ID = ?"
    data = (Menge, Preis, Lager, Waren_ID)
    cur.execute(sql_update_query, data)


updateMarkt(10, 0.99, "Nicht lieferbar", 4)

for row in cur.execute("SELECT * FROM Supermarkt"):
    print(row)

# addColumn = "ALTER TABLE decks ADD COLUMN Address text"
# cur.execute(addColumn)
# for row in cur.execute("SELECT * FROM decks"):
#     print(row)
#
##to drop tables
# cur.execute(
#     "CREATE TABLE decks_backup AS SELECT Short, Colors, FullName, Price, Wins FROM decks"
# )
# cur.execute("DROP TABLE decks")
# cur.execute("ALTER TABLE decks_backup RENAME TO decks")
#
#
# cur.execute("INSERT INTO decks VALUES ('Ur-Dragon','WUBRG','The Ur-Dragon',1347.29,30)")
# cur.execute(
#     "INSERT INTO decks VALUES ('Aegar','UR','Aegar, the Freezing FLame',160.34,2)"
# )
# for row in cur.execute("SELECT * FROM decks"):
#     print(row)
#
# cur.execute("SELECT * FROM decks")
# rows = cur.fetchall()
# for row in rows:
#     print(row)
#
# updateTable("Aegar", 209.5, 4)
# for row in cur.execute("SELECT * FROM decks"):
#     print(row)

db.commit()
db.close()
