def generate_alert(alert):
    if alert["alert_type"] == "Brute Force Suspected":
        print(
            f"[ALERT] {alert['alert_type']} for user {alert['username']}, "
            f"{alert['failures']} failed logins before success at {alert['success_time']}"
        )

    elif alert["alert_type"] == "Excessive Failed Logins":
        print(
            f"[ALERT] {alert['alert_type']} for user {alert['username']}, "
            f"{alert['failure_count']} failed login attempts detected"
        )

    else:
        print(f"[ALERT] {alert}")