# Linux Authentication Log Analyzer

A beginner-friendly cybersecurity project using Python and Bash.

## Objective
Analyze sample SSH authentication logs and count failed
password attempts by source IP address.

## Features
- Reads a sample authentication log.
- Extracts source IP addresses from failed login entries.
- Counts failed attempts per IP.
- Flags activity that reaches a configurable threshold.
- Provides a Bash script to run the analyzer.

## Requirements
- Python 3
- Bash

## How to Run

Run directly with Python:

    python3 analyzer.py

Run with Bash:

    chmod +x run.sh
    ./run.sh

## Configuration

Edit THRESHOLD in analyzer.py to change the alert threshold.

## Sample Data
The sample.log file contains synthetic training data.
No real systems are scanned or modified.

## Limitations
- Uses a simplified log format.
- Does not block IP addresses.
- A flagged IP is not necessarily malicious.
- Intended for educational and defensive security practice.

## Disclaimer
Use this project for authorized defensive security learning.
