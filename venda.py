class Venda:
    def __init__(self, conn):
        self.conn = conn

    def valida_item(self, id, lista):
            cur = self.conn.cursor()
            sql = "SELECT * FROM Vendas WHERE cliente_id = %s ORDER BY id DESC LIMIT 1;"

            cur.execute(sql, (id,))
            # Recuperar os resultados da consulta
            results = cur.fetchall()
            for row in results:
                id_venda = row[0]

            for dicionario in lista:
                nome = dicionario['nome']
                quantidade = dicionario['quantidade']
                id_produto = dicionario['id_produto']
                valor = dicionario['valor_unitario']
                quantidade_total_item = dicionario['quantidade_total_item']

                print(f'nome: {nome}, Quantidade: {quantidade}, id {id_produto}, valor unitario, {valor}')
                sql2 = "INSERT INTO ItensVenda (venda_id, produto_id, quantidade, valor_unitario) VALUES (%s, %s, %s, %s)"
                cur.execute(sql2, (id_venda, id_produto, quantidade, valor))
                self.conn.commit()

                quantidadeAtual = quantidade_total_item - quantidade

                sql3 = "UPDATE Produtos SET quantidade_estoque = %s WHERE id = %s"
                cur.execute(sql3, (quantidadeAtual, id_produto))  # Corrigido o parâmetro da consulta SQL
                self.conn.commit()
            cur.close()

    def efetua_compra(self, total, cliente, id, itens):
        print(f"A compra deu um total de {total} reais!\n")
        escolha = input("Quer continuar com a compra? (S/N): ")

        if escolha.lower() == "s":
            print("Como será sua opção de pagamento?")
            tipo_pagamento = input("Aceitamos, Cartões e dinheiro: ")

            sql = "INSERT INTO Vendas (cliente_id, total, tipo_pagamento) VALUES (%s, %s, %s)"
            cur = self.conn.cursor()
            cur.execute(sql, (id, total, tipo_pagamento))
            self.conn.commit()

            self.valida_item(id, itens)

            cur.close()
        else:
            print("Ok, muito obrigado!!")

    def compra_produto(self):
        ID = input("Informe o ID do cliente: ")
        nome = input("Informe o nome do cliente: ")

        cur = self.conn.cursor()
        B = True
        itens = []
        total = 0
        while B:
            item_id = input("Informe o ID do item desejado (ou pressione Enter para sair): ")
            if item_id:
                try:
                    item_id = int(item_id)  # Certifique-se de que o ID do item é um número inteiro
                    sql = "SELECT * FROM produtos WHERE id = %s"
                    cur.execute(sql, (item_id,))
                    # Recuperar os resultados da consulta
                    results = cur.fetchall()

                    for row in results:
                        id_produto = row[0]
                        nome_produto = row[1]
                        preco_produto = row[3]
                        quantidade_produto = row[4]
                        if quantidade_produto == 0:
                            print("Produto com falta em estoque :(")
                        else:
                            quantidade_compra = int(input("Informe quantidade desejada do item: "))
                            if quantidade_compra > quantidade_produto:
                                print(f"Essa quantidade não existe, temos apenas {quantidade_produto} unidades desse item!!")
                            else:
                                quantidade_produto -= 1
                                total += preco_produto * quantidade_compra
                                itens.append({'nome': nome_produto, 'quantidade': quantidade_compra, 'id_produto': id_produto, 'valor_unitario': preco_produto, 'quantidade_total_item': quantidade_produto})

                except ValueError:
                    print("Por favor, insira um ID de item válido (número inteiro).")
            if not item_id:
                B = False

        self.efetua_compra(total, nome, ID, itens)

        cur.close()

    def relatorio_cliente(self):
        ID = int(input("Informe o ID do cliente: "))
        cur = self.conn.cursor()
        sql = "SELECT COUNT(*) AS total_compras FROM Vendas WHERE cliente_id = %s"

        cur.execute(sql, (ID,))
        # Recuperar os resultados da consulta
        recset = cur.fetchall()
        for rec in recset:
            print(f"\nO cliente com o ID {ID} fez um total de {rec[0]} compras.\n")
        cur.close()
    def relatorio_empreendimento(self):
        cur = self.conn.cursor()
        sql = "SELECT COUNT(*) AS total_compras FROM Vendas"

        cur.execute(sql)
        # Recuperar os resultados da consulta
        recset = cur.fetchall()
        for rec in recset:
            print(f"\nO total de vendas do estabelecimento é {rec[0]}.\n")
        cur.close()



