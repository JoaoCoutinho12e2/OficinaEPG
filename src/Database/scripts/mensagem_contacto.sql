-- mensagem_contacto.sql



-- Criar mensagens de contacto
CREATE TABLE mensagem_contacto (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    assunto VARCHAR(150),
    mensagem TEXT NOT NULL,
    recebido_em TIMESTAMP WITH TIME ZONE DEFAULT now()
);
