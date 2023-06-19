num = input("Введите число: ")
n = len(num)
num = int(num)

sum = 0

while n > 0:
    sum += num % 10
    num //= 10
    n -= 1
print(sum)


