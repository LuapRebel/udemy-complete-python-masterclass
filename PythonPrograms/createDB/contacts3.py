import sqlite3

db = sqlite3.connect("contacts.sqlite")

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print("Name:", name)
    print("Phone:", phone)
    print("Email:", email)
    print("-" * 20)

db.close()