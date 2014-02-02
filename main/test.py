import sqlite3
db = sqlite3.connect('models/offers.db')
db.execute("CREATE TABLE offers (id INTEGER PRIMARY KEY,"+
    "department CHAR(10) NOT NULL,"
    +" course_number INTEGER NOT NULL,"
    +" price REAL NOT NULL,"
    +" description TEXT,"
    +" email CHAR(100) NOT NULL)")
db.execute("INSERT INTO offers (department,course_number, price, description, email) VALUES ('COMP', 0015, 150.50, 'Dirty', 'arlobclarke@gmail.com')")
db.execute("INSERT INTO offers (department,course_number, price, description, email) VALUES ('COMP', 0020, 120.50, 'Clean', 'arlobclarke@gmail.com')")

db.commit()

db2 = sqlite3.connect('models/bids.db')
db2.execute("CREATE TABLE bids (id INTEGER PRIMARY KEY, department CHAR(10) NOT NULL, course_number INTEGER NOT NULL, email CHAR(100) NOT NULL)")
db2.execute("INSERT INTO bids (department,course_number, email) VALUES ('COMP', 0020, 'arlobclarke@gmail.com')")
db2.commit()