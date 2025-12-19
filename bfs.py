from collections import deque
import time
from estado import No

def buscaLargura(grafo, inicio=0):
    numeroCidades = len(grafo)
    
    # Estado inicial
    noRaiz = No(
        cidadeAtual=inicio, 
        cidadesVisitadas={inicio}, 
        caminhoPercorrido=[inicio], 
        custoAcumulado=0, 
        estimativaHeuristica=0
    )
    
    fila = deque([noRaiz])
    
    contadorNosVisitados = 0
    tempoInicio = time.time()

    while fila:
        noAtual = fila.popleft()
        contadorNosVisitados += 1

        # Teste para verificar se já visitou todas as cidades
        if len(noAtual.cidadesVisitadas) == numeroCidades:
            custoRetorno = grafo[noAtual.cidadeAtual][inicio]
            tempoTotal = time.time() - tempoInicio
            
            return {
                "algoritmo": "BFS",
                "caminho": noAtual.caminhoPercorrido + [inicio],
                "custo": noAtual.custoAcumulado + custoRetorno,
                "visitados": contadorNosVisitados,
                "tempo": tempoTotal
            }

        # Expansão de vizinhos
        for vizinho in range(numeroCidades):
            if vizinho not in noAtual.cidadesVisitadas:
                novoCustoAcumulado = noAtual.custoAcumulado + grafo[noAtual.cidadeAtual][vizinho]
                novasCidadesVisitadas = noAtual.cidadesVisitadas.copy()
                novasCidadesVisitadas.add(vizinho)
                novoCaminho = noAtual.caminhoPercorrido + [vizinho]
                
                filho = No(vizinho, novasCidadesVisitadas, novoCaminho, novoCustoAcumulado, 0)
                fila.append(filho)
                
    return None