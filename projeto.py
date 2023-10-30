import psycopg
import cliente
    


def menu():
    print("|---------------------------|")
    print("| Olá, bem-vindo ao sistema |")
    print("|---------------------------|")
    print("| Escolha uma das opções    |")
    print("| abaixo para gerenciamento |")
    print("|---------------------------|")
    print("1- Cliente")
    print("2- Venda")
    print("3- Produto")
    print("4- Sair")


# Conectar ao seu banco de dados PostgreSQL
conn_string = "dbname=gerencia_empreendimento user=postgres password=postgres"
conn = psycopg.connect(conn_string)

# Abrir um cursor para realizar operações no banco de dados
cur = conn.cursor()

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
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
        print("Opção selecionada: Venda")
        # Aqui você pode adicionar a lógica para lidar com as operações de vendas

    elif opcao == "3":
        print("Opção selecionada: Produto")
        # Aqui você pode adicionar a lógica para lidar com as operações de produtos

    elif opcao == "4":
        print("Saindo do sistema. Obrigado!")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.\n")

# Fechar a conexão com o banco de dados
conn.close()
