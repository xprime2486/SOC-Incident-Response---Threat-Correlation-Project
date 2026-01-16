SOC Incident Response & Threat Correlation Project

soc-incident-response/
│
├── app.py
├── correlate.py
├── severity.py
├── requirements.txt
│
├── logs/
│   ├── auth.log
│   ├── firewall.log
│   └── web.log
│
├── templates/
│   └── dashboard.html
│
└── static/
    └── style.css


Project Overview

A SOC-style SIEM dashboard that analyzes authentication logs,
detects suspicious activity, and displays alerts in a web UI.Features
- Brute-force detection
- IP-based alerting
- Severity classification
- SOC-style dashboard UI

## 🛠 Tech Stack
- Python
- Flask
- HTML / CSS
- Log Analysis

- correlate.py
This file performs log correlation. It extracts IP addresses using regex and groups multiple security
events by IP, simulating SIEM behavior.

severity.py
Assigns Low, Medium, or High severity based on event frequency. This reflects real SOC incident
prioritization.

app.py
The Flask backend that connects all modules, processes incidents, and sends structured data to
the dashboard.  

dashboard.html
Displays incidents in a table with severity-based color coding to help analysts quickly assess
threats.

style.css
Provides visual clarity using colors and layout similar to SOC dashboards

How to Run
pip install -r requirements.txt
python app.py
