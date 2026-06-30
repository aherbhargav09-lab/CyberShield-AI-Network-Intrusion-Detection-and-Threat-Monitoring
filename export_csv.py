import csv
import sqlite3

conn = sqlite3.connect("database/alerts.db")
cursor = conn.cursor()

cursor.execute("""
SELECT id, attack_type, source_ip, timestamp
FROM alerts
ORDER BY id DESC
""")

rows = cursor.fetchall()

with open("alerts_report.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "ID",
        "Attack Type",
        "Source IP",
        "Timestamp"
    ])

    writer.writerows(rows)

conn.close()

print("CSV report created successfully!")
print("File: alerts_report.csv")
