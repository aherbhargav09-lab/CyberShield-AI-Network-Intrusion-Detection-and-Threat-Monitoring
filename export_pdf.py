import sqlite3

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer
from reportlab.platypus import Table
from reportlab.platypus import TableStyle

conn = sqlite3.connect("database/alerts.db")
cursor = conn.cursor()

cursor.execute("""
SELECT id, attack_type, source_ip, timestamp
FROM alerts
ORDER BY id DESC
""")

rows = cursor.fetchall()

conn.close()

pdf = SimpleDocTemplate("CyberShield_Report.pdf")

styles = getSampleStyleSheet()

elements = []

elements.append(
    Paragraph("<b>CyberShield AI Security Report</b>", styles["Title"])
)

elements.append(
    Spacer(1, 20)
)

table_data = [
    [
        "ID",
        "Attack",
        "Source IP",
        "Timestamp"
    ]
]

for row in rows:
    table_data.append(row)

table = Table(table_data)

table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.darkblue),
    ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("GRID", (0,0), (-1,-1), 1, colors.black),
    ("BACKGROUND", (0,1), (-1,-1), colors.beige),
    ("ALIGN", (0,0), (-1,-1), "CENTER"),
    ("BOTTOMPADDING", (0,0), (-1,0), 12),
]))

elements.append(table)

pdf.build(elements)

print("PDF Report Created Successfully!")
