def print_matrix(matrix: list[list[int]]):
    for line in matrix:
        print(*line)


def main():
    n = int(input("Digite o valor de n: "))
    matrix = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    print_matrix(matrix)


main()
