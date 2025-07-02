-- agendamentos.sql



-- Criar agendamentos
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