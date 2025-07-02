# Setup de Oficina EPG

Este guia explica tudo que é necessário para configurar e iniciar o projeto Django Oficina EPG localmente.

## Pré-requisitos

- Python 3.10+ instalado
- `virtualenv` ou `venv` disponível
- Git

## Clonar o projeto

1. **Clonar o repositório**:

    ```git
    git clone https://github.com/JoaoCoutinho12e2/OficinaEPG.git
    ```

2. **Abrir o VSCode no diretório do projeto clonado**

## Depois de clonar

1. **Ativar o ambiente virtual**

    ```bash
    python -m venv venv
    ```

2. Depois ativa o ambiente virtual:

- Linux/MacOS:

    ```zsh
    source venv/bin/activate
    ```

- Windows:

    ```cmd
    venv\Scripts\activate
    ```

### Instalação e servidor

1. Instalar as dependências do projeto:

    ```zsh
    pip install -r requirements.txt
    ```

2. Migrar os dados do projeto:

    ```zsh
    python manage.py migrate
    ```

3. Correr o servidor:

    ```zsh
    python manage.py runserver
    ```
