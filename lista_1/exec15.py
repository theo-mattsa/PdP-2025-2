QTD_NOTAS: int = 3


def main():
    notas = [0] * QTD_NOTAS
    pesos = [0] * QTD_NOTAS

    for i in range(QTD_NOTAS):
        nota = float(input(f"Nota {i}: "))
        peso = float(input(f"Peso {i}: "))
        notas[i], pesos[i] = nota, peso

    media = 0
    for i in range(QTD_NOTAS):
        media += notas[i] * pesos[i]

    print("Média do aluno: ", media)


main()
