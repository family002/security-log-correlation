from src.ingestion.auth_parser import parse_auth_log
from src.normalization.normalizer import normalize_event
from src.correlation.rules import detect_brute_force, detect_excessive_failures
from src.alerting.alert_generator import generate_alert
import os

def main():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    log_file = os.path.join(BASE_DIR, "data", "raw", "auth.log")
    raw_events = parse_auth_log(log_file)
    normalized_events = [normalize_event(event) for event in raw_events]
    
    brute_force_alerts = detect_brute_force(normalized_events)
    excessive_failure_alerts = detect_excessive_failures(normalized_events)
    alerts = brute_force_alerts + excessive_failure_alerts
    
    for alert in alerts:
        generate_alert(alert)

if __name__ == "__main__":
    main()