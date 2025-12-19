import random

def gerarMatrizDistancias(numeroCidades, seed=None):
    #Gera uma matriz NxN com pesos aleatórios.
    if seed is not None:
        random.seed(seed)

    matriz = []
    for i in range(numeroCidades):
        linha = []
        for j in range(numeroCidades):
            if i == j:
                linha.append(0)
            else:
                # Pesos aleatórios que vão variar entre 10 e 100
                linha.append(random.randint(10, 100)) 
        matriz.append(linha)
    return matriz

def imprimirMatriz(matriz):
    print("Matriz de Distâncias:")
    for linha in matriz:
        print(linha)
    print("-" * 30)