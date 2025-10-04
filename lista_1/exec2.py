VOGAIS = ["a", "e", "i", "o", "u"]


def is_vogal(letter: str) -> bool:
    return letter in VOGAIS


def main():
    foo: str = input()
    counter: int = 0
    for letter in foo:
        if is_vogal(letter):
            counter += 1
    print(counter)
