A = []
for i in range(1, 50):
    if i % 3 == 0:
        A.append(i)
print('Numbers divisible by 3: ', A)

B = []
for n in range(1, 50):
    if n % 4 == 0:
        B.append(n)
print('Numbers divisible by 4: ', B)

C = []
for m in range(1, 50):
    if m % 5 == 0:
        C.append(m)
print('Numbers divisible by 5: ', C)

D = []
for m in range(1, 50):
    if m % 7 == 0 and m % 5 == 0:
        D.append(m)
print('Numbers divisible by 3,4 and 5: ', D)
