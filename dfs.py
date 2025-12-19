import time
from estado import No

def buscaProfundidade(grafo, inicio=0):
    numeroCidades = len(grafo)
    
    noRaiz = No(
        cidadeAtual=inicio, 
        cidadesVisitadas={inicio}, 
        caminhoPercorrido=[inicio], 
        custoAcumulado=0, 
        estimativaHeuristica=0
    )
    
    pilha = [noRaiz]
    
    contadorNosVisitados = 0
    tempoInicio = time.time()

    while pilha:
        noAtual = pilha.pop()
        contadorNosVisitados += 1

        if len(noAtual.cidadesVisitadas) == numeroCidades:
            custoRetorno = grafo[noAtual.cidadeAtual][inicio]
            tempoTotal = time.time() - tempoInicio
            
            return {
                "algoritmo": "DFS",
                "caminho": noAtual.caminhoPercorrido + [inicio],
                "custo": noAtual.custoAcumulado + custoRetorno,
                "visitados": contadorNosVisitados,
                "tempo": tempoTotal
            }

        for vizinho in range(numeroCidades):
            if vizinho not in noAtual.cidadesVisitadas:
                novoCustoAcumulado = noAtual.custoAcumulado + grafo[noAtual.cidadeAtual][vizinho]
                novasCidadesVisitadas = noAtual.cidadesVisitadas.copy()
                novasCidadesVisitadas.add(vizinho)
                novoCaminho = noAtual.caminhoPercorrido + [vizinho]
                
                filho = No(vizinho, novasCidadesVisitadas, novoCaminho, novoCustoAcumulado, 0)
                pilha.append(filho)
    return None