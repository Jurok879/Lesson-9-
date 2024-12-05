def is_prime(func):
    def wrapper(*args):        # внутренняя функция
        sum_ = func(*args)
        prime = True
        for i in range(2, sum_):
            if sum_ % i == 0:
                prime = False
                break
        if prime:
            print('Простое')
        else:
            print('Составное')
        return sum_
    return wrapper


@is_prime                      # декоратор для функции sum_three
def sum_three(*args):
    return sum(args)



result = sum_three(2, 3, 6)
print(result)