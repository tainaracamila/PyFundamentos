""" Classe responsável por desenhar o boneco"""
class Enforcado(object):

	def __init__(self, chances = 6):
		self.chances = chances

	def getHomem(self, erros):

		if (erros == 1):
			print("0")
		elif(erros == 2):
			print("0")
		elif(erros == 3):
			print("0")
		elif(erros == 4):
			print("0")
		elif(erros == 5):
			print("0")
		else:
			print("0")

	def getWin(self):
		return print("\nFim de jogo, você ganhou!")

	def getGameOver(self):
		return print("\nFim de jogo, você perdeu!")

