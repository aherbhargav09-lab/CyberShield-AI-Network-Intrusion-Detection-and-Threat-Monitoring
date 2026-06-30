# CyberShield-AI-Network-Intrusion-Detection-and-Threat-Monitoring
# 🛡 CyberShield AI

# AI-Powered Network Intrusion Detection & Threat Monitoring System

CyberShield AI is a real-time Network Intrusion Detection and Threat Monitoring System developed using Python, Flask, Scapy, SQLite, and Chart.js. It captures live network traffic, detects suspicious activities such as SYN Flood and Port Scan attacks, stores alerts in a database, calculates the network risk level, and displays everything through an interactive web dashboard.

---

# 📌 Features

- ✅ Live Packet Capture
- ✅ SYN Flood Detection
- ✅ Port Scan Detection
- ✅ SQLite Alert Logging
- ✅ Risk Level Calculation
- ✅ Interactive Flask Dashboard
- ✅ Attack Statistics Chart
- ✅ CSV Report Export
- ✅ PDF Report Export
- ✅ Demo Mode for Hackathon Presentation

---

# 🏗 System Architecture

```
                Internet Traffic
                       │
                       ▼
            Scapy Packet Capture
                       │
                       ▼
             Detection Engine
          ┌──────────┴──────────┐
          │                     │
          ▼                     ▼
     SYN Flood             Port Scan
     Detection             Detection
          │                     │
          └──────────┬──────────┘
                     ▼
              SQLite Database
                     │
                     ▼
               Risk Engine
                     │
                     ▼
             Flask Dashboard
                     │
                     ▼
          CSV & PDF Report Export
```

---

# 🖥 Dashboard

The dashboard displays:

- 📦 Packets Captured
- 🚨 Total Alerts
- ⚠️ SYN Flood Count
- 🔎 Port Scan Count
- 🛡 Risk Level
- 📊 Attack Statistics Chart
- 📋 Recent Alerts Table

---

# 🛠 Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Core Programming |
| Flask | Web Framework |
| Scapy | Packet Capture |
| SQLite | Database |
| HTML | Frontend |
| CSS | Styling |
| Chart.js | Data Visualization |
| Kali Linux | Development Platform |

---

# 📂 Project Structure

```
CyberShield-AI/
│
├── app.py
├── test.py
├── setup_db.py
├── export_csv.py
├── export_pdf.py
├── requirements.txt
├── README.md
│
├── detector/
│   ├── packet_capture.py
│   ├── syn_flood.py
│   ├── port_scan.py
│   └── risk_engine.py
│
├── database/
│   ├── db.py
│   └── alerts.db
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── reports/
│
└── screenshots/
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/CyberShield-AI.git
```

---

## Move into Project

```bash
cd CyberShield-AI
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start Flask Dashboard

```bash
python3 app.py
```

---

## Start Packet Capture

```bash
sudo python3 test.py
```

---

## Open Dashboard

```
http://127.0.0.1:5000
```

---

# 📊 How It Works

### Step 1

Scapy captures live packets from the network interface.

↓

### Step 2

Each packet is analyzed by the detection engine.

↓

### Step 3

The system detects:

- SYN Flood Attacks
- Port Scan Attacks

↓

### Step 4

Detected attacks are stored in the SQLite database.

↓

### Step 5

The Risk Engine calculates the network risk level.

↓

### Step 6

The Flask Dashboard displays all information in real time.

---

# 📄 Report Generation

Generate CSV Report

```bash
python3 export_csv.py
```

Generate PDF Report

```bash
python3 export_pdf.py
```

---

# 📈 Dashboard Metrics

- Packets Captured
- Total Alerts
- SYN Flood Count
- Port Scan Count
- Risk Level
- Attack Statistics
- Recent Alerts

---

# 🚀 Future Scope

- AI/ML-based Attack Detection
- Email Notifications
- SMS Alerts
- Cloud Deployment
- Multi-user Authentication
- Threat Intelligence Integration
- SIEM Integration
- Real-time Alert Notifications

---

# 📷 Screenshots

Include screenshots of:

- Project Structure
- Flask Server
- Packet Capture
- Dashboard
- SQLite Alerts

---

# 👨‍💻 Developer

**Bhargav Aher**

Cyber Security Student

GitHub:
https://github.com/aherbhargav09-lab

---

# 📄 License

This project was developed for educational and hackathon purposes.

---

# ⭐ Acknowledgements

- Python
- Flask
- Scapy
- SQLite
- Chart.js
- Kali Linux

---

## ⭐ If you found this project useful, please consider giving it a Star on GitHub.
