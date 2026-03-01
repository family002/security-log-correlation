def parse_auth_log(file_path):
    # return [
    #     {"timestamp": "2026-02-07T10:00:00Z", "event_type": "login_failure", "username": "jdoe", "ip_address": "192.168.1.10"},
    #     {"timestamp": "2026-02-07T10:01:00Z", "event_type": "login_failure", "username": "jdoe", "ip_address": "192.168.1.10"},
    #     {"timestamp": "2026-02-07T10:02:00Z", "event_type": "login_success", "username": "jdoe", "ip_address": "192.168.1.10"},
    # ]
    events = []
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            timestamp, event_type, username, ip_address = line.split(",")
            events.append({
                "timestamp": timestamp,
                "event_type": event_type,
                "username": username,
                "ip_address": ip_address
            })
    return events