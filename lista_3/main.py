def head(l: list):
    # Retorna o primeiro elemento da lista
    return l[0]


def tail(l: list):
    # Retorno toda lista, exceto o primeiro elemento
    return l[1:]


def init(l: list):
    # Retorna toda a lista, exceto o ultimo elemento
    return l[:-1]


def last(l: list):
    # Retorna o ultimo elemento da lista
    return l[-1]


# Questão 05
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# Questão 06
def concat_list(l1: list, l2: list):
    if l1 == [] and l2 == []:
        return []
    if l1 == []:
        return concat_list(l2, [])
    return [head(l1)] + concat_list(tail(l1), l2)


# Questão 07
def in_list(value, l: list):
    if l == []:
        return False
    if value == head(l):
        return True
    return in_list(value, tail(l))


# Questão 08
def union_list(l1: list, l2: list):

    if l1 == [] and l2 == []:
        return []
    if l1 == []:
        return union_list(l2, [])

    if in_list(head(l1), l2) or in_list(head(l1), tail(l1)):
        return union_list(tail(l1), l2)

    return [head(l1)] + union_list(tail(l1), l2)


# Questão 09
def qtd_maiores(n: int, l: list):
    if l == []:
        return 0
    if head(l) > n:
        return 1 + qtd_maiores(n, tail(l))

    return qtd_maiores(n, tail(l))


# Questão 10
def get_maiores(n: int, l: int):

    if l == []:
        return []

    if head(l) > n:
        return concat_list([head(l)], get_maiores(n, tail(l)))

    return concat_list([], get_maiores(n, tail(l)))


# Questão 11 (usando head e concat)
def inverte_lista(l: list):
    if l == []:
        return []
    return concat_list([last(l)], inverte_lista(init(l)))


# Questão 12
def gera_palindromo(l: list):
    return concat_list(l, inverte_lista(l))


# print("".join(gera_palindromo(list("a noite"))))


# Questão 13
def len_list(l: list):
    if l == []:
        return 0
    return 1 + len_list(tail(l))


# Questão 14
def aux_primo(n: int, d: int):
    if n == d:
        return True
    if n % d == 0:
        return False
    return aux_primo(n, d + 1)


def ehPrimo(n: int):
    if n == 1:
        return False
    return aux_primo(n, 2)


# print(ehPrimo(4))


# Questão 15 (retira da segunda, tudo que há na primeira)
# l1 = [1, 2, 3] l2 = [3, 4, 5, 6]
def my_strip(l1: list, l2: list):
    if l2 == []:
        return []
    return concat_list(
        [head(l2)] if not in_list(head(l2), l1) else [], my_strip(l1, tail(l2))
    )


# print(my_strip([1, 2, 3, 5, 6], [3, 4, 5, 6]))


# Questão 16
# "sdd" "saudade"
def consoantList(l1: list, l2: list):
    aux = my_strip(l1, l2)
    return (len_list(l2) - len_list(aux)) == len_list(l1)
