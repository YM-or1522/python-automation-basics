server = {"name": "web01", "ip": "192.0.2.10", "port": 22}
print(server["name"])
server["status"] = "running"
print(server)
for key, value in server.items():
    print(f"{key} = {value}")
print(server.get("owner", "unknown"))