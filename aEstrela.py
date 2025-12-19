import heapq
import time
from estado import No, calcularHeuristica

def algoritmoAEstrela(grafo, inicio=0):
    numeroCidades = len(grafo)
    
    heuristicaInicial = calcularHeuristica(inicio, {inicio}, grafo)
    noRaiz = No(inicio, {inicio}, [inicio], 0, heuristicaInicial)
    
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
                "algoritmo": "A*",
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
                
                novaHeuristica = calcularHeuristica(vizinho, novasCidadesVisitadas, grafo)
                
                # No A*, custoTotalEstimado = custoAcumulado + heurística
                # (esse valor é calculado automaticamente dentro da classe No)
                filho = No(vizinho, novasCidadesVisitadas, novoCaminho, novoCustoAcumulado, novaHeuristica)
                heapq.heappush(fronteira, filho)
    return None