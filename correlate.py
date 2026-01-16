import re

def correlate_logs():
    incidents = {}

    log_sources = {
        "logs/auth.log": "Auth Failure",
        "logs/firewall.log": "Firewall Block",
        "logs/web.log": "Suspicious Web Request"
    }

    ip_pattern = r"\b\d{1,3}(?:\.\d{1,3}){3}\b"

    for file, event_type in log_sources.items():
        with open(file, "r") as f:
            for line in f:
                match = re.search(ip_pattern, line)
                if not match:
                    continue

                ip = match.group()

                if ip not in incidents:
                    incidents[ip] = {
                        "count": 1,
                        "events": [event_type]
                    }
                else:
                    incidents[ip]["count"] += 1
                    incidents[ip]["events"].append(event_type)

    return incidents

