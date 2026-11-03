total = 0
for i in range(1,11):
    total += i
print(total)

ports = [22, 80, 443, 8080, 3306]
for p in ports:
    if p < 1024:
        print(p)