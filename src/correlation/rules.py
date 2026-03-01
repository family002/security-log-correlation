# Brute Force Detection
def detect_brute_force(events):
    alerts = []
    user_events = {}
    for e in events:
        user  = e["username"]
        if user not in user_events:
            user_events[user] = []
        user_events[user].append(e)

    for user, ev_list in user_events.items():
        failures = [ev for ev in ev_list if ev["event_type"] == "login_failure"]
        success = [ev for ev in ev_list if ev["event_type"] == "login_success"]
        if len(failures) >= 2 and success:
            alerts.append({
                "alert_type": "Brute Force Suspected",
                "username": user,
                "failures": len(failures),
                "success_time": success[0]["timestamp"]
            })
    return alerts

# Excessive Failed Logins
def detect_excessive_failures(events):
    failure_counts = {}
    for event in events:
        if event["event_type"] == "login_failure":
            user = event["username"]
            failure_counts[user] = failure_counts.get(user, 0) + 1
    alerts = []
        
    for user, count in failure_counts.items():
        if count >= 3:
            alerts.append({
                "alert_type": "Excessive Failed Logins",
                "username": user,
                "failure_count": count
            })
    return alerts