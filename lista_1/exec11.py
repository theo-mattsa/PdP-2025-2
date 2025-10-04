# 100 50 20 10 5 2
CEDULAS_DISPONIVEIS = [100, 50, 20, 10, 5, 2, 1]


def main():
    valor = int(input("Saque em R$: "))
    if valor < 2:
        raise ValueError("O valor de saque precisa ser maior que R$ 2")

    cedulas = [{"valor": num, "quantidade": 0} for num in CEDULAS_DISPONIVEIS]

    for cedula in cedulas:
        qtd = valor // cedula["valor"]
        valor = valor % cedula["valor"]
        cedula["quantidade"] = qtd

    for cedula in cedulas:
        print(f"Quantidade em cédulas de R$ {cedula["valor"]}", cedula["quantidade"])


main()
