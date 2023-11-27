-- Criação da tabela de clientes
CREATE TABLE Clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    codigo INT NOT NULL
);

-- Criação da tabela de produtos
CREATE TABLE Produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    codigo INT NOT NULL,
    valor DECIMAL(10, 2) NOT NULL,
    quantidade_estoque INT NOT NULL
);

-- Criação da tabela de vendas
CREATE TABLE Vendas (
    id SERIAL PRIMARY KEY,
    cliente_id INT,
    codigo_cliente INT,
    total DECIMAL(10, 2) NOT NULL,
    tipo_pagamento VARCHAR(20) NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id)
);

-- Criação da tabela de itens de venda
CREATE TABLE ItensVenda (
    id SERIAL PRIMARY KEY,
    venda_id INT,
    produto_id INT,
    quantidade INT NOT NULL,
    valor_unitario DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (venda_id) REFERENCES Vendas(id),
    FOREIGN KEY (produto_id) REFERENCES Produtos(id)
);

-- Alteração na tabela de clientes para remover o campo codigo
ALTER TABLE Clientes DROP COLUMN codigo;

-- Alteração na tabela de produtos para remover o campo codigo
ALTER TABLE Produtos DROP COLUMN codigo;
