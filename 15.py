def DEL(x, y):
    return x%y == 0
def impl(x, y):
    return not x or y

A = 1
while True:
    f = True
    for x in range(100):
        f = f and impl(DEL(x, A) and DEL(x, 16), not DEL(x, 16) or DEL(x, 24))
    if f:
        print(A)
        break
    A += 1
a, b = 3, 5
for i in range(2*a - 10, 2*b + 10):
    x = i/2
    print(x, end=' ')