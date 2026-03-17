import sqlite3

DB = "nac_system.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS loadsheet(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT, flight TEXT,
        pax INTEGER, cargo REAL,
        zfw REAL, tow REAL, lw REAL,
        index_val REAL, cg REAL, stab TEXT
    )
    """)

    conn.commit()
    conn.close()

def insert_loadsheet(data):
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
    INSERT INTO loadsheet
    (date, flight, pax, cargo, zfw, tow, lw, index_val, cg, stab)
    VALUES (?,?,?,?,?,?,?,?,?,?)
    """, data)

    conn.commit()
    conn.close()
