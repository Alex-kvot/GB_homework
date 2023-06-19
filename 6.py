ticket = int(input("Номер билета:"))

first = ticket // 1000
second = ticket % 1000

print(first)
print(second)

first = str(first)
second = str(second)

total_f = int(first[0]) + int(first[1]) + int(first[2])
total_s = int(second[0]) + int(second[1]) + int(second[2])

if total_f == total_s:
    print("Yes")
else:
    print("No")