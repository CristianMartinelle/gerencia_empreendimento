import networkx as nx
import matplotlib.pyplot as plt

# Crie um objeto de grafo direcionado
G = nx.DiGraph()

def adicionar_vertice():
    # Solicita o nome do vértice
    nome_vertice = input("Digite o nome do vértice: ")
    # Adiciona o vértice ao grafo
    G.add_node(nome_vertice)

def adicionar_aresta():
    # Solicita os nomes dos vértices de origem e destino
    origem = input("Nome do vértice de origem: ")
    destino = input("Nome do vértice de destino: ")
    # Adiciona a aresta ao grafo
    G.add_edge(origem, destino)

while True:
    print("Escolha uma opção:")
    print("1. Adicionar vértice")
    print("2. Adicionar aresta")
    print("3. Visualizar o grafo")
    print("4. Sair")
    
    escolha = input("Digite o número da opção: ")
    
    if escolha == "1":
        adicionar_vertice()
    elif escolha == "2":
        adicionar_aresta()
    elif escolha == "3":
        # Visualiza o grafo
        nx.draw(G, with_labels=True, font_weight='bold')
        plt.show()
    elif escolha == "4":
        break
    else:
        print("Opção inválida. Tente novamente.")

# Fim do programa
