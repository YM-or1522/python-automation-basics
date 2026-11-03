ports = [22, 80, 443]
print(ports[0])
print(ports[-1])
ports.append(8000)
print(len(ports))
print(ports)
print(ports[:2])
print(22 in ports)
for p in ports:
    print(f"ports {p}")