import math

EPS = 10e-8
VAR = 24


def print_head():
    print(f'{"N":9}|\t{"h":9}|\t{"Integral":11}|\t{"Оценка погрешности":9}|\t{"k":15}|')


def print_res(n, h, integral, est, k):
    print(f'{n:9d}|\t{h:9f}|\t{integral:9.9f}|\t{est:18e}|\t{k:15e}|')


def f(x):
    if VAR == 20:
        return math.e ** x - x ** 2 + 1
    elif VAR == 24:
        return 2 * math.e ** x - 2 * x + 3
    else:
        return 0


# Формула Симпсона
def simpson_formula(a, n, h):
    _sum = 0
    for i in range(n):
        _a, _b = a + i * h, a + (i + 1) * h
        _sum += ((_b - _a) / 6) * (f(_a) + 4 * f((_a + _b) / 2) + f(_b))
    return _sum


# Формула Гаусса
def gauss_formula(a, n, h):
    k, a02, a1 = 0, 5 / 9, 8 / 9
    _sum = 0
    for i in range(n):
        k = a + (2 * i + 1) * h / 2
        _sum += (h / 2) * (a02 * f(k - h * math.sqrt(0.6) / 2) + a1 * f(k) + a02 * f(k + h * math.sqrt(0.6) / 2))
    return _sum


# Оценка погрешности
def calc_error(curSum, prevSum, tet):
    return (curSum - prevSum) * tet


# Эмпирическая оценка порядка аппроксимации
def calc_k(curSum, s0, s1):
    return math.log(abs((curSum - s0) / (s1 - s0) - 1)) / math.log(0.5)


def simpson_method(a, b):
    print('Формула Симпсона')
    print_head()
    n, h, curSum, prevSum = 1, 1, 0, 0
    error, tet, k = 1, 1 / 15, 0
    s0 = simpson_formula(a, n, h)
    s1 = simpson_formula(a, n * 2, h)
    count = 2
    while abs(error) > EPS:
        prevSum = curSum
        h = (b - a) / n
        curSum = simpson_formula(a, n, h)
        count += n
        error = calc_error(curSum, prevSum, tet)
        k = calc_k(curSum, s0, s1)
        s0, s1 = s1, curSum
        print_res(n, h, curSum, error, k)
        n *= 2
    print('Результат:', curSum)
    print('Кол-во обращений:', count)


def gauss_method(a, b):
    print('Формула Гаусса-3')
    print_head()
    n, h, curSum, prevSum = 1, 1, 0, 0
    error, tet, k = 1, 1 / 63, 0
    s0 = gauss_formula(a, n, h)
    s1 = gauss_formula(a, n * 2, h)
    count = 0
    while abs(error) > EPS:
        prevSum = curSum
        h = (b - a) / n
        curSum = gauss_formula(a, n, h)
        count += 3 * n
        error = calc_error(curSum, prevSum, tet)
        k = calc_k(curSum, s0, s1)
        s0, s1 = s1, curSum
        print_res(n, h, curSum, error, k)
        n *= 2
    print('Результат:', curSum)
    print('Кол-во обращений:', count)
