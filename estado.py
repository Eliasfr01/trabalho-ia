class No:
    def __init__(self, cidadeAtual, cidadesVisitadas, caminhoPercorrido, custoAcumulado=0, estimativaHeuristica=0):
        self.cidadeAtual = cidadeAtual
        self.cidadesVisitadas = cidadesVisitadas  # Cidades que já foram visitadas
        self.caminhoPercorrido = caminhoPercorrido      # Lista com a ordem das cidades
    
        # Quanto custou sair do início até aqui
        self.custoAcumulado = custoAcumulado      
        
        # Quanto acredita-se que falta para terminar
        self.estimativaHeuristica = estimativaHeuristica      
        
        # O custo total estimado do caminho
        self.custoTotalEstimado = custoAcumulado + estimativaHeuristica 

    def __lt__(self, outroNo):
        # É necessário para a fila de prioridade ordenar pelo menor custoTotalEstimado
        return self.custoTotalEstimado < outroNo.custoTotalEstimado

def calcularHeuristica(cidadeAtual, cidadesVisitadas, grafo):
    """
    Heurística do vizinho mais próximo:
    Retorna o custo da menor aresta saindo da cidade atual para uma cidade que ainda não foi visitada.
    """
    numeroCidades = len(grafo)
    
    # Se já visitou todas as cidades, a estimativa de custo restante é 0
    if len(cidadesVisitadas) == numeroCidades:
        return 0 
    
    menorCustoAresta = float('inf')
    
    for vizinho in range(numeroCidades):
        if vizinho not in cidadesVisitadas:
            custoViagem = grafo[cidadeAtual][vizinho]
            if custoViagem < menorCustoAresta:
                menorCustoAresta = custoViagem
                
    return menorCustoAresta if menorCustoAresta != float('inf') else 0