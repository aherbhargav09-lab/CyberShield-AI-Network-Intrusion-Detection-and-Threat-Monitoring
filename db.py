import sqlite3

DATABASE = "database/alerts.db"


def init_db():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alerts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        attack_type TEXT,
        source_ip TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS stats(
        id INTEGER PRIMARY KEY,
        packet_count INTEGER DEFAULT 0
    )
    """)

    cursor.execute("""
    INSERT OR IGNORE INTO stats(id, packet_count)
    VALUES(1,0)
    """)

    conn.commit()
    conn.close()


def insert_alert(attack_type, source_ip):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO alerts(attack_type,source_ip)
    VALUES(?,?)
    """,(attack_type,source_ip))

    conn.commit()
    conn.close()


def get_alerts():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM alerts
    ORDER BY id DESC
    """)

    alerts = cursor.fetchall()

    conn.close()

    return alerts


def get_alert_count():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM alerts
    """)

    count = cursor.fetchone()[0]

    conn.close()

    return count


# -------------------------
# Packet Counter Functions
# -------------------------

def update_packet_count():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    UPDATE stats
    SET packet_count = packet_count + 1
    WHERE id = 1
    """)

    conn.commit()

    conn.close()


def get_packet_count():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT packet_count
    FROM stats
    WHERE id = 1
    """)

    count = cursor.fetchone()[0]

    conn.close()

    return count


init_db()
