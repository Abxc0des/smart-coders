#60.fibonacci series

n = int(input("enter number of terms :"))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#61.harmonic series

n = int(input("enter n :"))
total = 0
for i in range(1, n + 1):
    total = total + 1 / i
print("sum :", total)

#62.alternating sum

n = int(input("enter n :"))
total = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        total = total - i
    else:
        total = total + i
print("sum :", total)

#63.power without pow

x = float(input("enter x :"))
n = int(input("enter n :"))
result = 1
for i in range(abs(n)):
    result = result * x
if n < 0:
    result = 1 / result
print("answer :", result)

#64.sum of factorials

n = int(input("enter n :"))
factorial = 1
total = 0
for i in range(1, n + 1):
    factorial = factorial * i
    total = total + factorial
print("sum of factorials :", total)

