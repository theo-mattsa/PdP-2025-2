def is_prime(num: int):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def main():
    a = int(input("Valor de a: "))
    b = int(input("Valor de b: "))

    primes = [num for num in range(a, b + 1) if is_prime(num)]
    print(*primes)


main()
