# coding=utf-8
import  math


EPSILON = 0.00000001
A = 1
B = 2
VARIANT =24




def f13(x,number_of_dif):
    if (number_of_dif == 0):
        return 3 ** x + 2*x - 2
    elif (number_of_dif == 1):
        return 2+math.log(3)*(3**x)
    else:
        return (math.log(3) ** number_of_dif) * (3 ** x)

def f20(x,number_of_dif):
    if (number_of_dif == 0):
        return math.e ** x - x*x + 1
    elif (number_of_dif == 1):
        return math.e ** x - 2 * x
    else:
        return math.e ** x - 2

def f24(x,number_of_dif):
    if (number_of_dif == 0):
        return 2*math.e ** x - 2*x + 3
    elif (number_of_dif == 1):
        return 2*math.e ** x - 2
    else:
        return 2*math.e ** x


def print_head_trapeze():
    print('Формула трапеций 0')
    print(' N   |   h    | Integral | Оценка погр.  |  k    |')


def print_result_trapeze(a, b, c, d, e):
    print(" ", a, ' |   ', b, '   | ', c, ' | ', d, '  |  ', e, '   |')


def trapeze_method_error(max_arg):
    if (VARIANT==13):
        return f13(max_arg, 2)
    elif (VARIANT==20):
        return f20(max_arg, 2)
    elif (VARIANT==24):
        return f24(max_arg, 2)


def trapeze_method():
    print_head_trapeze()
    amountOfParts = 1
    prev_trapeze_sum=0
    error = 1
    h = 0
    k = 0
    iterral = 0
    trapezeSum = 0
    s1=0
    s2=0


    while abs(error) > EPSILON:
        h = (B-A) / amountOfParts
        trapezeSum=trapeze_count_0(amountOfParts,h)
        if (amountOfParts > 1):
            error=(trapezeSum-prev_trapeze_sum)/3
        prev_trapeze_sum = trapezeSum

        if (amountOfParts > 2):
            k = math.log((trapezeSum - s1) / (s2 - s1) - 1) / math.log(0.5)
            print_result_trapeze(amountOfParts, h, trapezeSum, error, k)
        elif amountOfParts > 1:
            print_result_trapeze(amountOfParts, h, trapezeSum, error, ' ')
        else:
            print_result_trapeze(amountOfParts, h, trapezeSum, ' ', ' ')

        amountOfParts *= 2


        s1=s2
        s2=trapezeSum
        trapezeSum = 0
    amountOfParts//=2
    print('Результат: ', s2)
    print('Kobr: ', amountOfParts+1)


def trapeze_method_modified():
    print_head_trapeze()
    amountOfParts = 1
    prev_trapeze_sum=0
    error = 1
    h = 0
    k = 0
    trapezeSum = 0
    s1=0
    tmp=0
    s2=0

    while abs(error) > EPSILON:
        h = (B-A) / amountOfParts
        for j in range(1,amountOfParts):
            if (VARIANT==13):
                tmp+=f13(h*j+A,0)
            elif (VARIANT==20):
                tmp+=f20(h*j+A,0)
            elif (VARIANT==24):
                tmp+=f24(h*j+A,0)

            if (VARIANT == 13):
                trapezeSum=h*(0.5*(f13(A,0)+f13(B,0))+tmp)+h*h*(f13(A,1)-f13(B,1))/12
            elif (VARIANT==20):
                trapezeSum = h * (0.5 * (f20(A, 0) + f20(B, 0)) + tmp) + h * h * (f20(A, 1) - f20(B, 1)) / 12
            elif (VARIANT==24):
                trapezeSum = h * (0.5 * (f24(A, 0) + f24(B, 0)) + tmp) + h * h * (f24(A, 1) - f24(B, 1)) / 12
        tmp=0
        if (amountOfParts > 1):
            error=(trapezeSum-prev_trapeze_sum)/3
        prev_trapeze_sum = trapezeSum

        if (amountOfParts > 2):
            k = math.log((trapezeSum - s1) / (s2 - s1) - 1) / math.log(0.5)
            print_result_trapeze(amountOfParts, h, trapezeSum, error, k)
        elif amountOfParts > 1:
            print_result_trapeze(amountOfParts, h, trapezeSum, error, ' ')
        else:
            print_result_trapeze(amountOfParts, h, trapezeSum, ' ', ' ')

        amountOfParts *= 2


        s1=s2
        s2=trapezeSum
        trapezeSum = 0
    amountOfParts//=2
    print('Результат: ', s2)
    print('Kobr: ', amountOfParts+1)


def trapeze_count_0(amountOfParts, h):
    trapezeSum=0
    for i in range(0, amountOfParts):
        if (VARIANT==13):
            trapezeSum += ((h * (i + 1) + A) - (h * i + A)) * (f13(h * i + A, 0) + f13(h * (i + 1) + A, 0)) / 2
        elif (VARIANT==20):
            trapezeSum += ((h * (i + 1) + A) - (h * i + A)) * (f20(h * i + A, 0) + f20(h * (i + 1) + A, 0)) / 2
        elif (VARIANT==24):
            trapezeSum += ((h * (i + 1) + A) - (h * i + A)) * (f24(h * i + A, 0) + f24(h * (i + 1) + A, 0)) / 2

    return trapezeSum
