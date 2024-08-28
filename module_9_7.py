def is_prime(fun):
    def wrapper(*arg, **args):
        result = fun(*arg, **args)
        count = 0
        for i in range(1, result+1):
            if result % i == 0:
                count += 1
        if count == 2:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper


def sum_three(*arg):
    summ = sum(arg)
    return summ

result = is_prime(sum_three)
print(result(2, 3, 6))
