import unittest
from datetime import datetime, timezone
from src.correlation.rules import detect_brute_force, detect_excessive_failures
print("TEST FILE LOADED")

class TestCorrelation(unittest.TestCase):
    def test_brute_force_detection(self):
        events = [
            {
                "timestamp": datetime(2026, 2, 7, 10, 0, 0, tzinfo=timezone.utc),
                "event_type": "login_failure",
                "username": "user1",
                "ip_address": "192.168.1.10",
                "source": "auth_log"
            },
            {
                "timestamp": datetime(2026, 2, 7, 10, 1, 0, tzinfo=timezone.utc),
                "event_type": "login_failure",
                "username": "user1",
                "ip_address": "192.168.1.10",
                "source": "auth_log"
            },
            {
                "timestamp": datetime(2026, 2, 7, 10, 2, 0, tzinfo=timezone.utc),
                "event_type": "login_success",
                "username": "user1",
                "ip_address": "192.168.1.10",
                "source": "auth_log"
            }
        ]

        alerts = detect_brute_force(events)
        self.assertEqual(len(alerts), 1)
        self.assertEqual(alerts[0]["username"], "user1")

    def test_excessive_failures_detection(self):
        events = [
            {
                "timestamp": datetime(2026, 2, 7, 11, 0, 0, tzinfo=timezone.utc),
                "event_type": "login_failure",
                "username": "user2",
                "ip_address": "192.168.1.50",
                "source": "auth_log"
            },
            {
                "timestamp": datetime(2026, 2, 7, 11, 1, 0, tzinfo=timezone.utc),
                "event_type": "login_failure",
                "username": "user2",
                "ip_address": "192.168.1.50",
                "source": "auth_log"
            },
            {
                "timestamp": datetime(2026, 2, 7, 11, 2, 0, tzinfo=timezone.utc),
                "event_type": "login_failure",
                "username": "user2",
                "ip_address": "192.168.1.50",
                "source": "auth_log"
            }
        ]

        alerts = detect_excessive_failures(events)
        self.assertEqual(len(alerts), 1)
        self.assertEqual(alerts[0]["username"], "user2")
        self.assertIn("Excessive Failed Logins", alerts[0]["alert_type"])
        self.assertEqual(alerts[0]["failure_count"], 3)

if __name__ == "__main__":
    unittest.main()