from datetime import timedelta

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
    alerts = []
    user_events = {}
    for event in events:
        user = event["username"]
        user_events.setdefault(user, []).append(event)

    for user, ev_list in user_events.items():
        ev_list.sort(key=lambda x: x["timestamp"])
        for i in range(len(ev_list)):
            failures = 0
            start_time = ev_list[i]["timestamp"]
            for j in range(i , len(ev_list)):
                time_diff = ev_list[j]["timestamp"] - start_time
                if time_diff > timedelta(minutes=5):
                    break
                if ev_list[j]["event_type"] == "login_failure":
                    failures += 1
            if failures >= 3:
                alerts.append({
                    "alert_type": "Excessive Failed Logins",
                    "username": user,
                    "failure_count": failures,
                    "window_start": start_time.isoformat()
                })
                break
    return alerts