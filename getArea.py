from testRectangle import Rectangle, Square, Circle
a = int(input('Введите высоту прямоугольника:\t'))
b = int(input('Введите ширину прямоугольника:\t'))
c = int(input('Введите длину стороны квадрата:\t'))
r = int(input('Введите длину радиуса окружности:\t'))
print('--------------------------------------------')
r1 = Rectangle(a, b)
s2 = Square(c)
c3 = Circle(r)

figures = [r1, s2, c3]
for figure in figures:
    if isinstance(figure, Rectangle):
        print(f'Площадь прямоугольника равна: {figure.rectArea()}')
    elif isinstance(figure, Square):
        print(f'Площадь квадрата равна: {figure.sqrArea()}')
    else:
        print(f'Площадь окружности равна: {figure.circArea()}')