MAX = 10


def main():
    numbers: list[int] = []
    for _ in range(MAX):
        num = int(input())
        numbers.append(num)

    max_num = numbers[0]
    min_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    print(min_num, max_num)


main()
