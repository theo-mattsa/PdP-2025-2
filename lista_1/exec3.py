MAX: int = 5


def sort(listt: list[int]) -> None:
    n = len(listt)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if listt[j] > listt[j + 1]:
                listt[j], listt[j + 1] = listt[j + 1], listt[j]  # Pythonic swap


def main():
    numbers: list[int] = []
    for _ in range(MAX):
        num = int(input())
        numbers.append(num)
    sort(numbers)
    print("Sorted: ", numbers)


main()
