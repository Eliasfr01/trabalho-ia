import heapq
import time
from estado import No, calcularHeuristica

def buscaGulosa(grafo, inicio=0):
    numeroCidades = len(grafo)
    
    heuristicaInicial = calcularHeuristica(inicio, {inicio}, grafo)
    
    # No algoritmo guloso, vamos ignorar o custoAcumulado para decidir quem deve visitar.
    # É preciso guardar o custo real para exibir no final.
    # Obs: Passei 0 no custoAcumulado para que PriorityQueue ordene somente pela heurística,
    # mas é preciso recalcular o custo real no final.
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
            
            # Recalculando o custo real total (já que foi zerado no loop para priorizar a heurística)
            custoRealTotal = 0
            caminho = noAtual.caminhoPercorrido
            for i in range(len(caminho)-1):
                custoRealTotal += grafo[caminho[i]][caminho[i+1]]
            
            tempoTotal = time.time() - tempoInicio
            
            return {
                "algoritmo": "Gulosa",
                "caminho": noAtual.caminhoPercorrido + [inicio],
                "custo": custoRealTotal + custoRetorno,
                "visitados": contadorNosVisitados,
                "tempo": tempoTotal
            }

        for vizinho in range(numeroCidades):
            if vizinho not in noAtual.cidadesVisitadas:
                novasCidadesVisitadas = noAtual.cidadesVisitadas.copy()
                novasCidadesVisitadas.add(vizinho)
                novoCaminho = noAtual.caminhoPercorrido + [vizinho]
                
                novaHeuristica = calcularHeuristica(vizinho, novasCidadesVisitadas, grafo)
                
                # Foi passado custoAcumulado = 0.
                # Assim, custoTotalEstimado vai ser igual somente a heurística.
                filho = No(vizinho, novasCidadesVisitadas, novoCaminho, 0, novaHeuristica)
                heapq.heappush(fronteira, filho)
    return None