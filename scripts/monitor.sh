#!/bin/bash
while true; do
    cpu=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)
    mem=$(free | grep Mem | awk '{print $3/$2 * 100.0}')
    disk=$(df -h / | tail -1 | awk '{print $5}' | sed 's/%//')
    balance=$(curl -s http://localhost:5000/balance)
    echo "$(date): CPU=${cpu}%, MEM=${mem}%, DISK=${disk}%, BALANCE=${balance}" >> /var/log/wallet-scam.log
    if (( $(echo "$cpu > 80" | bc -l) )); then
        echo "ALERT: High CPU usage detected" | mail -s "Wallet Scam Alert" admin@example.com
    fi
    sleep 60
done
