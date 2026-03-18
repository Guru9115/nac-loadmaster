import sqlite3

DB = "nac_system.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    # Loadsheet table
    c.execute("""
    CREATE TABLE IF NOT EXISTS loadsheet(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT, flight TEXT,
        pax INTEGER, cargo REAL,
        zfw REAL, tow REAL, lw REAL,
        index_val REAL, cg REAL, stab TEXT
    )
    """)

    # LDM table (NEW)
    c.execute("""
    CREATE TABLE IF NOT EXISTS ldm(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        flight TEXT,
        pax INTEGER,
        zfw REAL,
        tow REAL,
        ldw REAL,
        fwd REAL,
        aft REAL
    )
    """)

    conn.commit()
    conn.close()


# ---------------- LOADSHEET SAVE ----------------
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


# ---------------- LDM SAVE ----------------
def insert_ldm(data):
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
    INSERT INTO ldm
    (date, flight, pax, zfw, tow, ldw, fwd, aft)
    VALUES (?,?,?,?,?,?,?,?)
    """, data)

    conn.commit()
    conn.close()
