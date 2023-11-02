import psycopg
import cliente
import produto
import os
import venda    

def menu():
    print("|---------------------------|")
    print("| Olá, bem-vindo ao sistema |")
    print("|---------------------------|")
    print("| Escolha uma das opções    |")
    print("| abaixo para gerenciamento |")
    print("|---------------------------|")
    print("1- Cliente")
    print("2- Produto")
    print("3- Venda")
    print("4- Sair")

# Conectar ao seu banco de dados PostgreSQL
conn_string = "dbname=gerencia_empreendimento user=postgres password=a4084b10"
conn = psycopg.connect(conn_string)

# Abrir um cursor para realizar operações no banco de dados
cur = conn.cursor()

while True:
    
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        os.system('cls')
        print("Opção selecionada: Cliente\n")
        cliente_instanciado = cliente.Cliente(conn)
        print("1-listar clientes")
        print("2-Adicionar cliente")
        print("3-Editar cliente")
        print("4-Remover cliente")

        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            cliente_instanciado.lista_clientes()
        elif escolha == "2":
            cliente_instanciado.adiciona_cliente()
        elif escolha == "3":
            cliente_instanciado.edita_cliente()
        elif escolha == "4":
            cliente_instanciado.remove_cliente()
        else:
            print("Comando inválido, voltando para tela inicial!!")

    elif opcao == "2":
        os.system('cls')
        print("Opção selecionada: Produto\n")
        produto_instanciado = produto.Produto(conn)
        print("1-listar produtos")
        print("2-Adicionar produtos")
        print("3-Editar produtos")
        print("4-Remover produtos")

        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            produto_instanciado.lista_produtos()
        elif escolha == "2":
            produto_instanciado.adiciona_produto()
        elif escolha == "3":
            produto_instanciado.edita_produto()
        elif escolha == "4":
            produto_instanciado.remove_produto()
        else:
            print("Comando inválido, voltando para tela inicial!!")

    elif opcao == "3":
        os.system('cls')
        print("Opção selecionada: Vendas\n")
        venda_instanciada = venda.Venda(conn)
        
        print("1-Vender")
        print("2-relatório cliente")
        print("3-relatório empreendimento")

        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            venda_instanciada.compra_produto()

        elif escolha == "2":
            venda_instanciada.relatorio_cliente()

        elif escolha == "3":
            venda_instanciada.relatorio_empreendimento()

    elif opcao == "4":
        os.system('cls')
        print("Saindo do sistema. Obrigado!")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.\n")

# Fechar a conexão com o banco de dados
conn.close()