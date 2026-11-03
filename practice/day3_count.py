ips = ["203.0.113.5", "198.51.100.7", "203.0.113.5", "203.0.113.5"]
counts = {}
for ip in ips:
    counts[ip] = counts.get(ip, 0) + 1
print(counts)