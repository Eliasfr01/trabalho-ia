from grafo import gerarMatrizDistancias, imprimirMatriz
from bfs import buscaLargura
from dfs import buscaProfundidade
from ucs import buscaCustoUniforme
from gulosa import buscaGulosa
from aEstrela import algoritmoAEstrela

def main():
    NUMERO_CIDADES = 8
    
    # Caso queira grafos aleatórios diferentes a cada execução, defina seed = None:
    seed = 30 
    
    print(f"--- Gerando Grafo com {NUMERO_CIDADES} cidades ---")
    print(f"--- ID da Execução (Seed): {seed} ---")
    
    # O grafo é gerado uma vez. Todos os algoritmos usarão este mesmo objeto 'grafo'.
    grafo = gerarMatrizDistancias(NUMERO_CIDADES, seed=seed)
    imprimirMatriz(grafo)
    
    print("\n--- Comparação (Todos usando o mesmo grafo acima) ---")
    
    resultados = []
    
    # Executa cada algoritmo passando o mesmo grafo gerado acima
    resultados.append(buscaLargura(grafo))
    resultados.append(buscaProfundidade(grafo))
    resultados.append(buscaCustoUniforme(grafo))
    resultados.append(buscaGulosa(grafo))
    resultados.append(algoritmoAEstrela(grafo))
    
    # Imprime Tabela Formatada
    print("\n" + "="*100)
    print(f"{'Algoritmo':<10} | {'Custo Total':<12} | {'Tempo (s)':<10} | {'Nós Visitados':<15} | {'Caminho'}")
    print("-" * 100)
    
    for r in resultados:
        if r:
            caminhoStr = str(r['caminho'])
            print(f"{r['algoritmo']:<10} | {r['custo']:<12} | {r['tempo']:<10.4f} | {r['visitados']:<15} | {caminhoStr}")
        else:
            print("Erro na execução")
    print("="*100)

if __name__ == "__main__":
    main()