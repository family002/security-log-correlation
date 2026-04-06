# Security Log Correlation & Threat Detection Engine

Senior project for CSE499.

This project ingests, normalizes, and correlates security logs to detect
suspicious behavior patterns such as brute-force authentication attempts.

## Overview

This project is a modular Security Log Correlation and Threat Detection Engine that simulates core functionality of a Security Information and Event Management (SIEM) system.

The system ingests authentication logs, normalizes events into a consistent format, applies rule-based correlation logic to detect suspicious behavior, and generates alerts. It also supports alert persistence and automated testing.

This project was developed as a senior capstone to demonstrate real-world cybersecurity and software engineering concepts.

## Features

### Core Features (Must-Have Requirements)

- **Log Ingestion**
- Reads authentication log data from a file
- Parses raw log entries into structured events

- **Event Normalization**
- Converts all events into a consistent schema
- Standard fields include timestamp, event type, username, IP address, and source

- **Brute-Force Detection**
- Detects multiple failed login attempts followed by a successful login

- **Human-Readable Alerts**
- Generates clear, formatted alerts in the console

- **Modular Architecture**
- Separates functionality into ingestion, normalization, correlation, and alerting modules

- **End-to-End Pipeline**
- Fully automated flow from log ingestion to alert generation

---

### Stretch Features
- **Real Log File Processing**
- Uses actual log files instead of hardcoded data

- **Multiple Detection Rules**
- Supports multiple independent threat detection strategies

- **Time-Based Detection**
- Detects suspicious activity within a defined time window (e.g., multiple failures within 5 minutes)

- **Alert Persistence**
- Saves alerts to a JSON file for later analysis

- **Automated Unit Tests**
- Includes tests to validate detection logic

---

### Project Structure
```markdown
security_log_correlation/
│
├── main.py
├── data/
│   ├── raw/
│   │   └── auth.log
│   └── alerts/
│       └── alerts.json
│
├── src/
│   ├── ingestion/
│   │   └── auth_parser.py
│   ├── normalization/
│   │   └── normalizer.py
│   ├── correlation/
│   │   └── rules.py
│   ├── alerting/
│   │   └── alert_generator.py
│   └── utils/
│
├── tests/
│   └── test_correlation.py
│
├── README.md
└── requirements.txt
```

---

## How It Works
1. **Ingestion**
    - Reads log data from auth.log

2. **Normalization**
    - Converts events into a standard format

3. **Correlation**
    - Applies detection rules:
        - Brute-force detection
        - Excessive failed login detection (time-based)

4. **Alerting**
    - Outputs alerts to the console
    - Saves alerts to alerts.json

---

## Example Output
```bash
[ALERT] Brute Force Suspected for user jdoe, 2 failed logins before success at 2026-02-07 10:02:00+00:00
[ALERT] Excessive Failed Logins for user asmith, 3 failed login attempts detected
```
## Running the Project
1. **Navigate to the project directory**
```bash
cd security_log_correlation
```
2. **Run the application**
```bash
python main.py
```
## Running Tests

To run unit tests:
```bash
python -m unittest discover -s tests
```
Expected output:
```bash
..
----------------------------------------------------------------------
Ran 2 tests in 0.00Xs

OK
```

---

## Technologies Used
- Python 3
- JSON (data storage)
- Standard Python libraries (datetime, os, unittest)
- Modular software architecture

---

## Challenges & Solutions
 - **Module Import Issues**
    - Resolved by restructuring project and using proper package initialization

- **File Path Errors**
    - Fixed using absolute paths with os.path

- **Datetime Serialization**
    - Converted datetime objects to ISO format before writing to JSON

- **Handling Multiple Alert Types**
    - Implemented dynamic alert formatting logic

---

## Future Improvements
- Web-based dashboard for alert visualization
- Support for additional log sources (e.g., web logs, system logs)
- Configurable detection rules via external configuration
- Advanced detection algorithms

**Author**<br>
Adam Arriola<br>
Computer Science Developer