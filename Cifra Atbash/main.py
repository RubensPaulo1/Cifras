ALFABETO = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
REVERSO_ALFABETO = ["z","y","x","w","v","u","t","s","r","q","p","o","n","m","l","k","j","i","h","g","f","e","d","c","b","a"]

def crip(mensagem):
	temp = []
	for i, letra in enumerate(mensagem):
		indc = 0
		while(indc < len(ALFABETO)):
			if(letra == ALFABETO[indc]):
				temp.append(REVERSO_ALFABETO[indc])
				break
			indc += 1 			
	return temp

def descrip(mensagem):
	temp = []
	for i, letra in enumerate(mensagem):
		indc = 0
		while(indc < len(ALFABETO)):
			if(letra == REVERSO_ALFABETO[indc]):
				temp.append(ALFABETO[indc])
				break
			indc += 1 			
	return temp

def entrada():
	while(True):
		mensagem  = input("Digite a mensagem:").lower()
		if mensagem.isalpha():
			return mensagem
		else:
			print("Digite apenas letras")

def main():

	while(True):
		print("[1] - Criptografar")
		print("[2] - Desriptografar")
		print("[3] - Sair")
		op = input(":")

		if(op == "1"):
			mensagem = entrada()
			msg = crip(mensagem)
			print("".join(msg))
		elif(op == "2"):
			mensagem = entrada()
			msg = descrip(mensagem)
			print("".join(msg))
		elif(op == "3"):
			print("Tchau!")
			break


if __name__ == '__main__':
				main()			