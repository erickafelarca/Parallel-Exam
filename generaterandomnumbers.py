import random

MyList = []

for i in range(0, 100):
    x = random.randint(100, 999)
    MyList.append(x)

    if i % 9 == 0:
        MyList.append(i)

print('Random Numbers: ', MyList)

print('\nNumbers divisible by 9: ', MyList)


def isDigitPresent(m, n):
    while m > 0:

        if m % 10 == n:
            break

        m = m / 10

    return m > 0


def printNumbers(num1, num2):
    for num in range(0, num1 + 1):

        if num == num2 or isDigitPresent(num, d):
            print(num, end=" ")


n = 999
d = 9
print("\nNumbers contain 9 digit: ")
printNumbers(n, d)
print()

print("\nPrime numbers: ")

for val in range(x):
    if val > 1:
        for i in range(2, val):
            if (val % i) == 0:
                break
        else:
            print(val, end=" ")
