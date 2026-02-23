from arte import logo
LISTA_ALFABETICA = [
        "a","b","c","d","e","f","g","h","i","j",
        "k","l","m","n","o","p","q","r","s","t",
        "u","v","w","x","y","z"
    ]

def cifrar(frase, indice):
    codificado = []
    for carac in frase:
        if carac not in LISTA_ALFABETICA:
            codificado.append(carac)
            continue

        x = 0
        while(x < len(LISTA_ALFABETICA)):
            if(LISTA_ALFABETICA[x] == carac):
                if(x + indice >= 26):
                    y = (x + indice) - 26
                    codificado.append(LISTA_ALFABETICA[y])
                    x = x + 1
                    break
                codificado.append(LISTA_ALFABETICA[x+indice])
            x = x + 1
    return codificado

def decifrar(frase, indice):
    codificado = []
    for carac in frase:
        if carac not in LISTA_ALFABETICA:
            codificado.append(carac)
            continue
        x = 0
        while(x < len(LISTA_ALFABETICA)):
            if(LISTA_ALFABETICA[x] == carac):
                if(x - indice < 0):
                    y = 26 + (x - indice)
                    codificado.append(LISTA_ALFABETICA[y])
                    x = x + 1
                    break
                codificado.append(LISTA_ALFABETICA[x-indice])
            x = x + 1
    return codificado

def input_cifra():
    while(True):
        cifra = input("Escolha um número de 1 a 26:")
        if not cifra.isdigit():
            print("Digite apenas números")
            continue   
        cifra = int(cifra)
        if(1 <= cifra <= 26):
            return cifra

def menu():
    while(True):
        logo()
        print("[1] - Codificar")
        print("[2] - decodificar")
        print("[3] - sair")
        op = input("")
        if(op == '1'):
            mensagem = input("Mensagem:")
            cifra = input_cifra()     
            a = cifrar(mensagem.lower(), cifra)
            print("".join(a))

        if(op == '2'):
            mensagem = input("Mensagem:")
            cifra = input_cifra()
            a = decifrar(mensagem.lower(), cifra)
            print("".join(a))

        if(op == '3'):
            break    

if __name__ == "__main__":
    menu()    