import string

def encrypt(text: str, key: str) -> str:
    len_key = len(key)
    len_letters = len(string.ascii_lowercase)

    res = ''

    for index, let in enumerate(text):
        key_let = key[index % len_key]
        padding = string.ascii_lowercase.index(key_let)

        let_index = string.ascii_lowercase.index(let)

        res += string.ascii_lowercase[(let_index + padding) % len_letters]

    return res

def decode(text: str, key: str) -> str:
    len_key = len(key)
    len_letters = len(string.ascii_lowercase)

    res = ''

    for index, let in enumerate(text):
        key_let = key[index % len_key]
        padding = string.ascii_lowercase.index(key_let)

        let_index = string.ascii_lowercase.index(let)

        res += string.ascii_lowercase[(let_index - padding) % len_letters]

    return res

def main() -> None:
    key = input("key: ").strip().lower()
    text = input("text: ").strip().lower()
    isencrypt = int(input("decode or encrypt(0/1): "))

    if isencrypt:
        res = encrypt(text=text, key=key)
    else:
        res = decode(text=text, key=key)

    print(res)


if __name__ == "__main__":
    main()