MAX: int = 5


# FIX IT
def sort(listt: list[int]) -> None:
    list_size = len(listt)
    for i in range(list_size):
        for j in range(list_size - i - 1):
            if listt[i] > listt[j]:
                temp = listt[i]
                listt[i] = listt[j]
                listt[j] = temp


numbers: list[int] = []

for _ in range(MAX):
    num = int(input())
    numbers.append(num)

sort(numbers)
print(numbers)
