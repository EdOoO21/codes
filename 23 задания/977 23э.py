def f(x, y):
    if x == y:
        return 1
    if x > y or x == 40:
        return 0
    if x < y:
        return f(x + 1, y) + f(x * 3, y) + f(x * 5, y)


print(f(1, 20) * f(20, 100))
