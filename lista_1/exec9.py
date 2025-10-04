DIM: int = 3


def print_matrix(matrix: list[list[int]]):
    for line in matrix:
        print(*line)


def main():
    matrix = [
        [int(input(f"Linha {i}, Coluna {j}: ")) for j in range(DIM)] for i in range(DIM)
    ]

    transposta = [[matrix[j][i] for j in range(DIM)] for i in range(DIM)]

    print("Transposta: ")
    print_matrix(transposta)


main()
