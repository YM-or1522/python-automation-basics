lines = [
    "Failed password for root from 203.0.113.5",
    "Accepted password for taro from 192.0.2.10",
    "Failed password for admin from 198.51.100.7",
]
failed = 0
for line in lines:
    if "Failed" in line:
        failed += 1
print(f"Failed: {failed}")