def f(x, y):
    if x == y:
        return 1
    if x > y or x == 90:
        return 0
    if x < y:
        return f(x + 1, y) + f(x * 2, y) + f(x * 3, y)


print(f(3, 30) * f(30, 100) * f(100, 184))
