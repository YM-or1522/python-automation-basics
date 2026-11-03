threshold = 80
usage =int(input("Disk usage (%): "))
if usage >= threshold:
    print(f"WARNING: disk usage is {usage}")
else:
    print(f"OK: disk usage is {usage}")