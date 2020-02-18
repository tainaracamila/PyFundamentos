import random
from enforcado import Enforcado

""" Retorna uma palavra aleatoria """
def getPalavra(arrayPalavras):
	return random.choice(arrayPalavras)

""" Retorna a posicao da letra """
def getPosicao(letra, palavraChaveValor):
	
	posicoes = []

	for indice, valor in palavraChaveValor:
		if (valor == letra):
			posicoes.append(indice)

	return posicoes

""" Funcao geral de formatacao de palavras/letras """
def formataPalavra(palavra):
	string = ''

	for c in palavra:
		string += c+" "
	
	return string

""" Funcao principal """
def main():

	arrayPalavras = []
	acertos = erros = 0
	arrayErros = []
	auxiliar = []

	enf = Enforcado()

	with open('palavras.txt', 'r') as palavras:
		for p in palavras:
			#tratamento para quebra de linha
			p = p.replace("\n","")
			arrayPalavras.append(p)

	palavra = getPalavra(arrayPalavras)
	palavraChaveValor = list(enumerate(palavra))
	
	# iniciando o array auxiliar com tracos de acordo com a palavra escolhida
	for l in palavra:
		auxiliar.append("_")

	print ("\nBem Vindo ao Jogo da Forca!\n")
	while True:
		
		# imprime o homem

		# imprime as letras erradas 
		if (arrayErros):
			print ("\nLetras erradas: "+formataPalavra(arrayErros))

		# imprime a palavra atualizada
		print("\n"+formataPalavra(auxiliar))

		letra = input("\nDigite uma letra: ")

		if letra in palavra:
			posicoes = getPosicao(letra, palavraChaveValor)
			
			#atualizando o array auxiliar
			for pos in posicoes:
				auxiliar[pos] = letra

			#atualizando contador de acertos
			acertos += len(posicoes)
			
			if (acertos == len(palavra)):
				enf.getWin()
				print("\nPalavra certa: "+palavra)
				break
			else:
				pass		
		else:
			erros += 1
			arrayErros.append(letra)

			if (erros == 6):
				#imprimir homem
				enf.getGameOver()
				print("\nPalavra certa: "+palavra)
				break
			else:
				pass


if __name__ == '__main__':
	main()


