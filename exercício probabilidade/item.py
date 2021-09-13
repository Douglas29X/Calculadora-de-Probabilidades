class Relatorio:

	def __init__(self, item):
		calculado = item.calcula_chance()

		print(f'\nA chance de você conseguir o item com as informações dadas é de {calculado}%\n')

		porcentagem = 30

		tentativa = 1

		for resposta in range(0,10):

			calculo = None

			while calculo != porcentagem:
				calculo = int((1 - ( 1 - item._numerador/item._denominador)**tentativa) * 100)
				tentativa+= 1

			if calculo == porcentagem:
				print(f'Para você ter {porcentagem}% de chances de conseguir o item\nvocê deverá matar {tentativa}'
					' inimigos no jogo')
				
				if porcentagem < 90:
					porcentagem+= 10
				elif porcentagem == 90:
					porcentagem += 5
				elif porcentagem == 95:
					porcentagem += 2
				elif porcentagem == 97:
					porcentagem = 100
		

class Item:
	def __init__(self, respostas):
		probabilidade = respostas.probabilidade
		self._probabilidade = probabilidade

		#fatiamento
		barra = str.find(probabilidade, '/')

		self._numerador = int(probabilidade[:barra])
		self._denominador = int(probabilidade[barra+1:])

		self._tentativas = int(respostas.tentativas)

	@property
	def probabilidade(self):
		return self._probabilidade

	@property
	def tentativas(self):
		return self._tentativas

	def calcula_chance(self):
		calculo = int((1 - ( 1 - self._numerador/self._denominador)**self._tentativas) * 100)
		return calculo

	def gera_relatorio(self):
		relatorio = Relatorio(self)