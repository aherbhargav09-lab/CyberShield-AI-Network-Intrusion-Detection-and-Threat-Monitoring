from database.db import insert_alert
from flask import redirect
from flask import Flask, render_template

from database.db import (
    get_alerts,
    get_alert_count,
    get_packet_count
)

from detector.risk_engine import calculate_risk

app = Flask(__name__)


@app.route("/")
def home():

    alerts = get_alerts()

    total_alerts = get_alert_count()

    packet_count = get_packet_count()
    
    print(packet_count)

    risk_level = calculate_risk(total_alerts)

    syn_count = 0
    port_scan_count = 0

    for alert in alerts:

        if alert[1] == "SYN Flood":
            syn_count += 1

        elif alert[1] == "Port Scan":
            port_scan_count += 1

    return render_template(
        "index.html",

        alerts=alerts,

        packet_count=packet_count,

        total_alerts=total_alerts,

        syn_count=syn_count,

        port_scan_count=port_scan_count,

        risk_level=risk_level
    )
@app.route("/demo/syn")
def demo_syn():

    insert_alert(
        "SYN Flood",
        "192.168.181.100"
    )

    return redirect("/")


@app.route("/demo/port")
def demo_port():

    insert_alert(
        "Port Scan",
        "192.168.181.101"
    )

    return redirect("/")

if __name__ == "__main__":

    app.run(debug=True)
