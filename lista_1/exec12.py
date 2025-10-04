def get_fatorial(num: int):

    if num == 0:
        return 1

    result: int = num
    for i in range(num - 1, 1, -1):
        result *= i

    return result


def main():

    n = int(input("Digite valor de n: "))
    if n < 0:
        raise ValueError("Digite um valor >= 0")

    print(f"{n}! = ", get_fatorial(n))


main()
