def collect_prime_numbers(high):
    """The function fills global_prime_numbers; called again, adds new numbers only.
    It is called by function 'prime'."""

    global global_prime_numbers

    if not global_prime_numbers:
        global_prime_numbers = [2]
        start = 3
    else:
        start = global_prime_numbers[-1] + 2

    for val in range(start, high + 1, 2):  # only the odd numbers
        is_prime = True
        sqrt_val = val ** 0.5
        for j in range(1, len(global_prime_numbers)):  # dividing only by prime numbers, without 2
            if global_prime_numbers[j] > sqrt_val:  # it's enough to divide to square root
                break
            if val % global_prime_numbers[j] == 0:
                is_prime = False
                break
        if is_prime:
            global_prime_numbers.append(val)


def prime(low, high):
    """The function uses global_prime_numbers and returns numbers from 'low' to 'high'"""

    global global_prime_numbers
    collect_prime_numbers(high)
    result = []
    for i in global_prime_numbers:
        if low <= i <= high:
            result.append(i)
    return result


def factorization(value):
    """The function returns prime numbers which are factors of 'val'"""

    prime_numbers = prime(2, value)
    if value in (0, 1) or value in prime_numbers:
        return [value]

    result = []
    v = value
    for p in prime_numbers:
        while v % p == 0:
            result.append(p)
            v = v // p
            if v in prime_numbers:
                result.append(v)
                v = 1
        if v == 1:
            break
    return result


def test_factorization(value):
    product = 1
    factors = factorization(value)
    for f in factors:
        product *= f
    return (product == value), factors


def test_factorization_in_range(max_val):
    most_factors = []
    most_factor_value = None
    is_ok = True
    for value in range(1, max_val + 1):
        res, factors = test_factorization(value)
        is_ok = is_ok and res
        if len(factors) > len(most_factors):
            most_factors = factors
            most_factor_value = value
    return is_ok, most_factor_value, most_factors


global_prime_numbers = []


# test
def main():
    print(prime(3, 15))
    print(prime(1, 18))
    print(prime(100, 200))
    print(prime(900, 100000))
    print(prime(20000, 30000))

    print('Factorization test in range 1000: ', test_factorization_in_range(1000))
    print('Factorization test in range 8000: ', test_factorization_in_range(8000))


if __name__ == '__main__':
    main()