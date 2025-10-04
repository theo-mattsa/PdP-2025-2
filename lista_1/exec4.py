def main():
    sum = 0
    number = int(input())
    digits_array = list(str(number))
    for num in digits_array:
        sum += int(num)
    print(sum)


main()
