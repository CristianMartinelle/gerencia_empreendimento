class Cliente:
    def __init__(self, conn):
        self.conn = conn

    def adiciona_cliente(self):
        cur = self.conn.cursor()
        nome = input("Informe o nome: ")
        telefone = input("Informe o telefone: ")
        cod = input("Informe o código: ")
        sql = "INSERT INTO clientes (nome, telefone, codigo) VALUES (%s, %s, %s)"
        cur.execute(sql, (nome, telefone, cod))
        self.conn.commit()
        cur.close()

    def remove_cliente(self):
        cur = self.conn.cursor()
        ID = input("Informe o ID: ")
        sql = "DELETE FROM clientes WHERE id = %s;"
        cur.execute(sql, (ID,))
        self.conn.commit()
        cur.close()

    def edita_cliente(self):
        cur = self.conn.cursor()
        ID = input("Informe o ID do cliente que deseja editar: ")
        novo_nome = input("Informe o novo nome (deixe em branco para manter o atual): ")
        novo_telefone = input("Informe o novo telefone (deixe em branco para manter o atual): ")
        novo_cod = input("Informe o novo código (deixe em branco para manter o atual): ")

        sql = "UPDATE clientes SET"
        params = []

        if novo_nome:
            sql += " nome = %s,"
            params.append(novo_nome)
        if novo_telefone:
            sql += " telefone = %s,"
            params.append(novo_telefone)
        if novo_cod:
            sql += " codigo = %s,"
            params.append(novo_cod)

        # Remover a última vírgula da consulta SQL e adicionar a condição WHERE
        sql = sql.rstrip(",") + " WHERE id = %s"
        params.append(ID)

        cur.execute(sql, params)
        self.conn.commit()
        cur.close()

    def lista_clientes(self):
        cur = self.conn.cursor()
        ID = input("Informe o ID do cliente que deseja buscar (deixe em branco caso não queira): ")
        nome = input("Informe o nome (deixe em branco caso não queira): ")
        telefone = input("Informe o telefone (deixe em branco caso não queira): ")
        cod = input("Informe o código (deixe em branco caso não queira): ")
        
        sql = "select * from clientes where "
        C = 0
        params = []
        if ID:
            sql += "ID = %s AND "
            params.append(ID)
            C += 1
        if nome:
            sql += "nome = %s AND "
            params.append(nome)
            C += 1
        if telefone:
            sql += "telefone = %s AND "
            params.append(telefone)
            C += 1
        if cod:
            sql += "codigo = %s AND "
            params.append(cod)
            C += 1
            
        sql = sql.rstrip("AND ")
        if C == 0:
            sql = "select * from clientes"
        cur.execute(sql,params)
        # Recuperar os resultados da consulta
        recset = cur.fetchall()
        for rec in recset:
            print(rec)