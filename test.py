# Нахождение простого числа
a = int(input("Введите число "))
if a > 1:
    for i in range(2, a):
        if (a % i) == 0:
            print("Не простое")
            break
    else:
        print("Простое")
else:
    print("Не простое")


# <-------------->
# генератор
def squares(n):
    i = 1
    while (i <= n):
        yield i ** 2
        i += 1


for i in squares(7):
    print(i)


# <-------------->
def star_triangle(r):
    for x in range(r):
        print(' ' * (r - x - 1) + '*' * (2 * x + 1))


star_triangle(7)


# <-------------->
# Пример *args
def sample(*args):
    print(args)


sample('time', 1, True)


# Пример **kwargs
def sample(**kwargs):
    print(kwargs)


sample(a='time', b=1)


def squares(n):
    i = 1
    while (i <= n):
        yield i ** 2
        i += 1


for i in squares(7):
    print(i)

# Пример лямбда-функции

test = lambda x, y: x * y
print(test(2, 4))

# Пример печати с конца

string = 'this is a string'
print(string[::-1])
