import sqlite3

db = sqlite3.connect("contacts.sqlite")

name = input("Please enter a username: ")

db_query = "SELECT * FROM contacts WHERE name LIKE ?"

for row in db.execute(db_query, (name,)):
    print(row)

# for name, phone, email in db.execute("SELECT * FROM contacts"):
#     print("Name:", name)
#     print("Phone:", phone)
#     print("Email:", email)
#     print("-" * 20)

db.close()
