#!/usr/bin/env bash
set -euo pipefail

DOMAIN="${1:?Usage: $0 domain}"

EXPIRY_DATE=$(echo | openssl s_client -servername "$DOMAIN" -connect "$DOMAIN:443" 2>/dev/null \
    | openssl x509 -noout -enddate | cut -d= -f2)

EXPIRY_SECONDS=$(date -d "$EXPIRY_DATE" +%s)
NOW_SECONDS=$(date +%s)

DAYS_LEFT=$(( (EXPIRY_SECONDS - NOW_SECONDS) / 86400 ))

echo "Certificate for $DOMAIN expires in $DAYS_LEFT days"

if (( DAYS_LEFT < 30 )); then
    echo "WARNING: Certificate expires soon!"
    exit 1
fi
