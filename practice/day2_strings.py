line = "  Failed password for root from 203.0.113.5  "
clean = line.strip()
print(clean)
print("Failed" in clean)
print(clean.split())
print(clean.upper())
service = "ssh"
port = 22
print(f"Service {service} uses port {port}")