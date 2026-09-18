#88.number triangle

n = int(input("enter n :"))
for i in range(1, n + 1):
    print(str(i) * i)

#89.sequential number triangle

n = int(input("enter n :"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#90.floyd triangle

n = int(input("enter number of rows :"))
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num = num + 1
    print()

#91.1 0 triangle

n = int(input("enter n :"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j % 2 == 0:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()

#92.pascal triangle

n = int(input("enter number of rows :"))
for i in range(n):
    value = 1
    print(" " * (n - i), end="")
    for j in range(i + 1):
        print(value, end=" ")
        value = value * (i - j) // (j + 1)
    print()

#93.number pyramid

n = int(input("enter n :"))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#94.inverted number triangle

n = int(input("enter n :"))
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#95.column increment

n = int(input("enter n :"))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i, end=" ")
    print()

#96.reverse number triangle

n = int(input("enter n :"))
for i in range(1, n + 1):
    for j in range(n, i - 1, -1):
        print(j, end=" ")
    print()

#97.binary triangle

n = int(input("enter n :"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print((i + j) % 2, end=" ")
    print()

