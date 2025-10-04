def main():
    word = input("Digite a palavra: ")
    if word[::-1] == word:
        print("É um palíndromo")
    else:
        print("Não é um palíndromo")


main()
