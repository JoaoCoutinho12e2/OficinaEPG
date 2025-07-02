-- servicos.sql



-- Criar serviços
CREATE TABLE servicos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    imagem_url TEXT,
    preco NUMERIC(10,2) NOT NULL CHECK (preco >= 0)
);