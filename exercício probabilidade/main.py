from item import Item, Relatorio

class RespostasUsuario:
	probabilidade = input('Qual a probabilidade do item ser obtido?'
		' (Coloque um valor fracionário, como "1/170")\n')
	tentativas = input('Quantas vezes você derrotou o inimigo para tentar conseguir o item? \n')

def inicia_programa():
	respostas = RespostasUsuario()
	item = Item(respostas)
	item.gera_relatorio()

if __name__ == '__main__':
	inicia_programa()