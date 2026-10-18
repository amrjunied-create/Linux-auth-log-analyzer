import re
from collections import Counter
from pathlib import Path

LOG_FILE = Path("sample.log")
THRESHOLD = 3


def analyze_log():
    if not LOG_FILE.exists():
        print(f"Error: {LOG_FILE} not found.")
        return

    failed_attempts = Counter()

    with LOG_FILE.open("r", encoding="utf-8") as file:
        for line in file:
            if "Failed password" not in line:
                continue

            match = re.search(
                r"from (\d{1,3}(?:\.\d{1,3}){3})",
                line
            )

            if match:
                ip = match.group(1)
                failed_attempts[ip] += 1

    print("=== Linux Authentication Log Analyzer ===")
    print(f"IPs with failed logins: {len(failed_attempts)}")
    print("\nFailed login counts:")

    for ip, count in failed_attempts.most_common():
        status = "SUSPICIOUS" if count >= THRESHOLD else "Normal"
        print(f"{ip}: {count} attempt(s) - {status}")


if __name__ == "__main__":
    analyze_log()
