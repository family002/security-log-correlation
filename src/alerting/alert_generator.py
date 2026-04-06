import json
import os

def generate_alert(alert):
    if "Brute Force Suspected" in alert["alert_type"]:
        print(
            f"[ALERT] {alert['alert_type']} for user {alert['username']}, "
            f"{alert['failures']} failed logins before success at {alert['success_time']}"
        )

    elif "Excessive Failed Logins" in alert["alert_type"]:
        print(
            f"[ALERT] {alert['alert_type']} for user {alert['username']}, "
            f"{alert['failure_count']} failed login attempts detected"
        )

    else:
        print(f"[ALERT] {alert}")

    save_alert(alert)

def serialize_alert(alert):
    serialized = {}
    for key, value in alert.items():
        if hasattr(value, "isoformat"):
            serialized[key] = value.isoformat()
        else:
            serialized[key] = value
    return serialized


def save_alert(alert):
    os.makedirs("data/alerts", exist_ok=True)
    file_path = "data/alerts/alerts.json"

    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            try:
                alerts = json.load(f)
            except json.JSONDecodeError:
                alerts = []
    else:
        alerts = []
    alerts.append(serialize_alert(alert))
    with open(file_path, "w") as f:
        json.dump(alerts, f, indent=4)