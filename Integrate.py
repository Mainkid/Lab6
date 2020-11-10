import math
from scipy.misc import derivative

eps = 10e-8
var = 24


def print_head():
    print(f'{"N":9}|\t{"h":9}|\t{"Integral":9}|\t{"Оценка погрешности":9}|\t{"k":15}|')


def print_res(n, h, integral, est, k):
    print(f'{n:9d}|\t{h:9f}|\t{integral:9f}|\t{est:18e}|\t{k:15e}|')


def f(x):
    if var == 20:
        return math.e ** x - x ** 2 + 1
    elif var == 24:
        return 2 * math.e ** x - 2 * x + 3
    else:
        return 0


def simpson_formula(a, n, h):
    _sum = 0
    for i in range(n):
        _a, _b = a + i * h, a + (i + 1) * h
        _sum += ((_b - _a) / 6) * (f(_a) + 4 * f((_a + _b) / 2) + f(_b))
    return _sum


def gauss_formula(a, b, n, h):
    pass


def simpson_method(a, b):
    print('Формула Симпсона')
    print_head()
    n, h, curSum, prevSum = 1, 1, 0, 0
    error, tet, k = 1, 1 / 15, 0
    s0 = simpson_formula(a, n, h)
    s1 = simpson_formula(a, n * 2, h)
    count = 2
    while abs(error) > eps:
        prevSum = curSum
        h = (b - a) / n
        curSum = simpson_formula(a, n, h)
        count += n
        error = (curSum - prevSum) * tet
        k = math.log(abs((curSum - s0) / (s1 - s0) - 1)) / math.log(0.5)
        s0 = s1
        s1 = curSum
        print_res(n, h, curSum, error, k)
        n *= 2
    print('Результат:', curSum)
    print('Кол-во обращений:', count)


def gauss_method(a, b):
    print('Формула Гаусса')
    print_head()
