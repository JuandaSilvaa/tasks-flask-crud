
# ✅ CRUD de Tarefas com Flask

Este projeto foi desenvolvido como parte do módulo de **Desenvolvimento de APIs com Flask** da Rocketseat. Ele consiste em uma **API REST** para o gerenciamento de tarefas, permitindo realizar operações de **CRUD** (Criar, Ler, Atualizar e Deletar) utilizando o **Flask**. As tarefas são armazenadas em **memória**, sem a utilização de banco de dados.

Além disso, o projeto inclui **testes automatizados** utilizando o framework **Pytest**, garantindo o correto funcionamento das operações da API e fornecendo uma camada extra de segurança ao refatorar ou adicionar novos recursos.


## 📌 Funcionalidades

- 📝 **Criar uma nova tarefa**
- 👀 **Visualizar lista de tarefas**
- 🔍 **Visualizar uma tarefa específica**
- ✏️ **Atualizar o nome, descrição e status de uma tarefa**
- 🗑 **Deletar uma tarefa**

## 🚀 Tecnologias Utilizadas

- Python 3.13.2
- Flask 
- Swagger (para documentação)
- Pytest (para testes automatizados)

## 📂 Estrutura do Projeto

```
tasks-flask-crud/
├─ models/
│  └─ task.py
├─ .gitignore
├─ app.py
├─ requirements.txt
├─ swagger-lista-tarefas-yaml
└─ tests.py
```

## 📝 Como Executar o Projeto

1. **Clone o repositório**:

   Clone este repositório executando o seguinte comando no terminal:

   ```bash
   git clone https://github.com/JuandaSilvaa/tasks-flask-crud.git
   ```

2. **Navegue até a pasta do projeto**:

   ```bash
   cd tasks-flask-crud
   ```

3. **Instale as dependências**:

   Certifique-se de ter o **Python** e o **pip** instalados em sua máquina. Em seguida, instale todas as dependências do projeto, incluindo o **pytest**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a API**:

   Execute o comando abaixo para iniciar o servidor Flask:

   ```bash
   python app.py
   ```

   Isso iniciará o servidor na URL `http://127.0.0.1:5000/`.

5. **Documentação Swagger**:

   O arquivo `swagger-lista-tarefas-yaml` contém a documentação da API e pode ser importado para o [Swagger Editor](https://editor.swagger.io/) ou para o Postman para facilitar o uso da API.

## 🧪 Testes Automatizados

Os testes automatizados foram feitos com o framework **Pytest**, que já está incluído no arquivo `requirements.txt`. Para executá-los, siga os passos abaixo:

1. **Execute os testes**:

   OBS: execute em um terminal separado

   Execute o comando para rodar os testes:

   ```bash
   pytest tests.py
   ```

   Isso executará todos os testes definidos no arquivo `tests.py`, garantindo que as operações de CRUD funcionem corretamente.

## ⚗️ O que é testado?

O arquivo `tests.py` contém testes para todas as operações principais da API:

- 📝 **Criar uma nova tarefa**: Verifica se uma nova tarefa é criada com sucesso.
- 👀 **Obter todas as tarefas**: Verifica se a lista de tarefas é retornada corretamente.
- 🔍 **Obter uma tarefa específica**: Verifica se uma tarefa específica pode ser recuperada usando o ID.
- ✏️ **Atualizar uma tarefa**: Verifica se é possível atualizar os dados de uma tarefa existente.
- 🗑 **Deletar uma tarefa**: Verifica se uma tarefa pode ser deletada corretamente.



