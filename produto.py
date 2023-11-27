class Produto:
    def __init__(self, conn):
        self.conn = conn

    def adiciona_produto(self):
        cur = self.conn.cursor()
        nome = input("Informe o nome: ")
        valor = input("Informe o valor: ")
        qntd_estoque = int(input("Informe a quantidade em estoque: "))
        sql = "INSERT INTO produtos (nome, valor, quantidade_estoque) VALUES (%s, %s, %s)"
        cur.execute(sql, (nome, valor, qntd_estoque))
        self.conn.commit()
        cur.close()

    def remove_produto(self):
        cur = self.conn.cursor()
        ID = input("Informe o ID: ")
        sql = "DELETE FROM produtos WHERE id = %s;"
        cur.execute(sql, (ID,))
        self.conn.commit()
        cur.close()

    def edita_produto(self):
        cur = self.conn.cursor()
        ID = input("Informe o ID do produto que deseja editar: ")
        novo_nome = input("Informe o novo nome (deixe em branco para manter o atual): ")
        novo_valor = input("Informe o novo valor (deixe em branco para manter o atual): ")
        nova_qntd_estoque = input("Informe a nova quantidade em estoque (deixe em branco para manter o atual): ")

        sql = "UPDATE produtos SET"
        params = []

        if novo_nome:
            sql += " nome = %s,"
            params.append(novo_nome)
        if novo_valor:
            sql += " valor = %s,"
            params.append(novo_valor)
        if nova_qntd_estoque:
            sql += " quantidade_estoque = %s,"
            params.append(nova_qntd_estoque)

        # Remova a vírgula extra e adicione a condição WHERE
        sql = sql.rstrip(",") + " WHERE id = %s"
        params.append(ID)

        cur.execute(sql, params)
        self.conn.commit()
        cur.close()

    def lista_produtos(self):
        cur = self.conn.cursor()
        ID = input("Informe o ID do produto que deseja buscar (deixe em branco caso não queira): ")
        nome = input("Informe o nome (deixe em branco caso não queira): ")
        
        sql = "SELECT * FROM produtos WHERE "
        params = []
        C = 0
        if ID:
            sql += "ID = %s AND "
            params.append(ID)
            C += 1
        if nome:
            sql += "nome = %s AND "
            params.append(nome)
            C += 1
            
        sql = sql.rstrip("AND ")
        if C == 0:
            sql = "SELECT * FROM produtos"
        cur.execute(sql, params)
        # Recuperar os resultados da consulta
        recset = cur.fetchall()
        for rec in recset:
            print(rec)
        print("\n")
