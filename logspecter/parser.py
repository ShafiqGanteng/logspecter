import re

IP_REGEX = re.compile(
    r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
)

LEVELS = [
    "INFO",
    "WARNING",
    "ERROR",
    "DEBUG",
    "CRITICAL"
]


def parse_line(line: str) -> dict:

    result = {
        "level": None,
        "ip": None,
        "message": line.strip()
    }

    for level in LEVELS:
        if level in line:
            result["level"] = level
            break

    ip_match = IP_REGEX.search(line)

    if ip_match:
        result["ip"] = ip_match.group()

    return result