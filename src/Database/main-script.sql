-- main-script.sql

-- Tabela de roles (funções de utilizador)
CREATE TABLE roles (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL UNIQUE
);

-- Tabela de utilizadores
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role_id INTEGER NOT NULL REFERENCES roles(id) ON DELETE RESTRICT,
    criado_em TIMESTAMP WITH TIME ZONE DEFAULT now()
);

-- Tabela de serviços
CREATE TABLE servicos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    imagem_url TEXT,
    preco NUMERIC(10,2) NOT NULL CHECK (preco >= 0)
);

-- Tabela de agendamentos
CREATE TABLE agendamentos (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    nome_cliente VARCHAR(100) NOT NULL,
    email_cliente VARCHAR(100) NOT NULL,
    telefone_cliente VARCHAR(20),
    servico_id INTEGER NOT NULL REFERENCES servicos(id) ON DELETE RESTRICT,
    data_hora TIMESTAMP WITH TIME ZONE NOT NULL,
    observacoes TEXT
);

-- Tabela de mensagens de contacto
CREATE TABLE mensagem_contacto (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    assunto VARCHAR(150),
    mensagem TEXT NOT NULL,
    recebido_em TIMESTAMP WITH TIME ZONE DEFAULT now()
);
