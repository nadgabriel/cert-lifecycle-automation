# Cert Lifecycle Automation

Automation toolkit for TLS certificate validation and renewal.

## Features

- Certificate expiration check (Bash + OpenSSL)
- Automated renewal logic (Python)
- CI/CD integration ready
- Container-friendly design

## Project Structure

scripts/
    check_cert.sh
    renew_cert.py

## Usage

Check certificate:

    ./scripts/check_cert.sh example.com

Renew certificate:

    python3 scripts/renew_cert.py

## Requirements

- Python 3.11+
- OpenSSL
- certbot (optional)

## CI/CD

Designed for GitLab CI or GitHub Actions pipeline integration.

## Author

Gabriel – DevOps & Network Automation
