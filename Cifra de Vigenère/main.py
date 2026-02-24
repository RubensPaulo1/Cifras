import string

ALFABETO = list(string.ascii_lowercase)
MOD = len(ALFABETO)


def gerar_chave_numerica(senha: str, tamanho_mensagem: int) -> list[int]:
    """
    Gera a chave numérica repetindo a senha até o tamanho desejado.
    Ex: 'minato' -> [12, 8, 13, 0, 19, 14, ...]
    """
    senha = senha.lower()
    if not senha or any(ch not in ALFABETO for ch in senha):
        raise ValueError("A senha deve conter apenas letras (a-z) e não pode ser vazia.")

    return [ALFABETO.index(senha[i % len(senha)]) for i in range(tamanho_mensagem)]


def criptografar(mensagem: str, senha: str) -> str:
    """
    Cifra de Vigenère (a-z).
    Mantém espaços e símbolos.
    Preserva maiúsculas/minúsculas.
    """
    chave = gerar_chave_numerica(senha, len(mensagem))
    resultado = []
    j = 0  # avança só quando é letra

    for ch in mensagem:
        if ch.lower() in ALFABETO:
            idx = ALFABETO.index(ch.lower())
            x = (idx + chave[j]) % MOD
            letra_cifrada = ALFABETO[x]
            resultado.append(letra_cifrada.upper() if ch.isupper() else letra_cifrada)
            j += 1
        else:
            resultado.append(ch)

    return "".join(resultado)


def descriptografar(mensagem_cifrada: str, senha: str) -> str:
    """
    Desfaz a cifra de Vigenère (a-z).
    Mantém espaços e símbolos.
    Preserva maiúsculas/minúsculas.
    """
    chave = gerar_chave_numerica(senha, len(mensagem_cifrada))
    resultado = []
    j = 0

    for ch in mensagem_cifrada:
        if ch.lower() in ALFABETO:
            idx = ALFABETO.index(ch.lower())
            y = (idx - chave[j]) % MOD
            letra = ALFABETO[y]
            resultado.append(letra.upper() if ch.isupper() else letra)
            j += 1
        else:
            resultado.append(ch)

    return "".join(resultado)


def main():
    mensagem = input("Digite sua mensagem: ")
    senha = input("Digite uma palavra aleatória (senha): ")

    try:
        cifrada = criptografar(mensagem, senha)
        original = descriptografar(cifrada, senha)

        print("\nCriptografada:   ", cifrada)
        print("Descriptografada:", original)

    except ValueError as e:
        print("\nErro:", e)


if __name__ == "__main__":
    main()