def normalize_event(event):
    return {
        "timestamp": event.get("timestamp"),
        "event_type": event.get("event_type"),
        "username": event.get("username"),
        "ip_address": event.get("ip_address"),
        "source": "auth_log"
    }