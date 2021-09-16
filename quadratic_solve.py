a = int(input('a =\t'))
b = int(input('b =\t'))
c = int(input('c =\t'))
def D(a, b, c):
    return b ** 2 - 4 * a * c

def quadratic_solve(a, b, c):
    if D(a, b, c) < 0:
        return 'Уравнение не имеет вещественных корней'
    elif D(a, b, c) == 0:
        x = -b / (2 * a)
        return f'Уравнение имеет один корень {x}'
    elif D(a, b, c) > 0:
        y = (-b - D(a, b, c) ** 0.5) / (2 * a)
        z = (-b + D(a, b, c) ** 0.5) / (2 * a)
        return f'Уравнение имеет два корня: {y} и {z}'

print(D(a, b, c))
print(quadratic_solve(a, b, c))