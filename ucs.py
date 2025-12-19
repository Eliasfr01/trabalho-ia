import heapq
import time
from estado import No

def buscaCustoUniforme(grafo, inicio=0):
    numeroCidades = len(grafo)
    
    noRaiz = No(inicio, {inicio}, [inicio], 0, 0)
    
    # Fila de Prioridade sempre vai remover quem tem menor custoTotalEstimado
    # No caso do UCS, custoTotalEstimado = custoAcumulado já que a heurística é 0
    fronteira = []
    heapq.heappush(fronteira, noRaiz)
    
    contadorNosVisitados = 0
    tempoInicio = time.time()

    while fronteira:
        noAtual = heapq.heappop(fronteira)
        contadorNosVisitados += 1

        if len(noAtual.cidadesVisitadas) == numeroCidades:
            custoRetorno = grafo[noAtual.cidadeAtual][inicio]
            tempoTotal = time.time() - tempoInicio
            
            return {
                "algoritmo": "UCS",
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
                
                # Heurística é 0 no UCS
                filho = No(vizinho, novasCidadesVisitadas, novoCaminho, novoCustoAcumulado, 0)
                heapq.heappush(fronteira, filho)
    return None