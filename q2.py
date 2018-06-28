def cria(qts_linhas,qtd_colunas):
	tadMatriz = []
	for i in range(qts_linhas):
		tadMatriz.append([])
		for j in range(qtd_colunas):
			tadMatriz[i].append([])
	return tadMatriz

def getElem(tadMatriz, linha, coluna):
	return tadMatriz[linha][coluna]

def setElem(tadMatriz, linha, coluna, valor):
	if len(tadMatriz) > linha and len(tadMatriz[0]) > coluna:
		tadMatriz[linha][coluna] = valor
		return tadMatriz
	else:
		return None

def soma (tadMatrizA,tadMatrizB):
	tadMatriz = []
	if len(tadMatrizA) == len(tadMatrizB) and len(tadMatrizA[0]) == len(tadMatrizB[0]):
		for i in range(tadMatrizA):
			tadMatriz.append[]
			for j range(tadMatrizA):
				tadMatriz[i].append(tadMatrizA[i][j]+tadMatrizA[i][j])
		return tadMatriz
	else:
		return None

def vezesK(tadMatriz, k):
	for i in range(tadMatriz):
		for j in range(tadMatriz[0]):
			tadMatriz = getElem(tadMatriz, linha, coluna)*k
	return tadMatriz

def main(args):
	print(cria(3,3))
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
