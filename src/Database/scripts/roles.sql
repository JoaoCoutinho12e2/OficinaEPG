-- roles.sql



-- Criar roles
CREATE TABLE roles (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL UNIQUE -- ex: 'admin', 'user'
);