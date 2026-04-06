from datetime import datetime

def normalize_event(event):
    return {
        "timestamp": datetime.fromisoformat(event.get("timestamp").replace("Z", "+00:00")),
        "event_type": event.get("event_type"),
        "username": event.get("username"),
        "ip_address": event.get("ip_address"),
        "source": "auth_log"
    }