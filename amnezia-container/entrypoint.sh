#!/bin/bash
set -e

if ! lsmod | grep -q amneziawg; then
    modprobe amneziawg || true
fi

sysctl -w net.ipv4.ip_forward=1
sysctl -w net.ipv4.conf.all.src_valid_mark=1

for conf in $WG_PATH/*.conf; do
    if [ -f "$conf" ]; then
        echo "Bringing up $conf"
        wg-quick up "$conf" || true
    fi
done

tail -f /dev/null
