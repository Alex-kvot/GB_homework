n = int(input("Количеcтво долек по горизонтали:"))
m = int(input("Количество долек по вертикали:"))

k = int(input("Сколько долек нужно отломить:"))

if k < n*m and (k % n == 0 or k % m == 0):
    print("Yes")
else:
    print("No")
