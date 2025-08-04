# Sistema Bancário Otimizado com Funções e Estruturas de Dados (V2)

## Visão Geral do Projeto

Este documento detalha a **Versão 2 (V2)** do sistema bancário desenvolvido como parte do **Bootcamp Santander 2025 - Back-end com Python**. Esta versão representa uma otimização e expansão significativa da V1, focando na modularidade do código através do uso de funções e na introdução de estruturas de dados para gerenciar usuários e contas de forma mais robusta.

O projeto visa consolidar os conhecimentos adquiridos nos módulos mais avançados do bootcamp, aplicando-os em um cenário prático de um sistema bancário.

## Contexto do Desenvolvimento

A V2 do sistema bancário foi desenvolvida após a conclusão do **Módulo 3 - Estruturas de Dados e Listas com Python** e **Módulo 4 - Trabalhando com Funções em Python**. As otimizações e novas funcionalidades implementadas nesta versão refletem diretamente o aprendizado desses módulos, transformando a estrutura monolítica da V1 em um código mais organizado e escalável.

## Objetivo Geral da V2

O principal objetivo da V2 foi aprimorar a estrutura do código existente, refatorando as operações de saque, depósito e extrato em funções dedicadas. Adicionalmente, para aprimorar a gestão de clientes e contas, foram implementadas duas novas funcionalidades essenciais: o cadastro de usuários e a criação de contas correntes, com a devida vinculação entre eles.

## Conceitos de Python Abordados na V2 com Exemplos do Código (`Otimizando o Sistema Bancário com Funções Python - Sistema_Bancario_v2`)

Esta seção detalha os conceitos de Python aplicados na V2, com exemplos diretos do arquivo `Otimizando o Sistema Bancário com Funções Python - Sistema_Bancario_v2`.

### Funções

A modularização do código foi o pilar da V2, com todas as operações principais encapsuladas em funções. O desafio propôs regras específicas para a passagem de argumentos em cada função, exercitando diferentes padrões:

#### Funções para Operações Existentes (Saque, Depósito, Extrato)

-   **Função `verificacao_saque` (Argumentos Apenas por Nome - Keyword-Only Arguments)**:
    Esta função é responsável por toda a lógica de saque. Receber argumentos apenas por nome (`*`) força o chamador a usar a sintaxe `parametro=valor`, o que aumenta a clareza e evita erros de ordem dos argumentos, especialmente em funções com muitos parâmetros.
    ```python
    def verificacao_saque(*, saque, saques_realizados_atual, LIMITE_SAQUE, VALOR_MAXIMO_SAQUE, saldo_atual, extrato_atual):
        # ... lógica de saque ...
        return saldo_atual, extrato_atual, saques_realizados_atual
    ```
    **Exemplo de Chamada no `sistema_bancario_v2.py`**:
    ```python
    saldo, extrato, saques_realizados = verificacao_saque(saque= saque, saques_realizados_atual= saques_realizados, LIMITE_SAQUE= LIMITE_SAQUE, VALOR_MAXIMO_SAQUE= VALOR_MAXIMO_SAQUE, saldo_atual= saldo, extrato_atual= extrato)
    ```
    Neste exemplo, cada argumento é explicitamente nomeado, tornando a chamada da função autoexplicativa.

-   **Função `verificacao_deposito` (Argumentos Apenas por Posição - Positional-Only Arguments)**:
    Esta função lida com a lógica de depósito. O uso de argumentos apenas por posição (`/`) antes dos parâmetros garante que eles sejam passados na ordem exata definida na assinatura da função, sem a possibilidade de serem nomeados. Isso é útil para APIs que precisam manter uma interface estável mesmo que os nomes internos dos parâmetros mudem.
    ```python
    def verificacao_deposito(saldo_atual, deposito, extrato_atual, /):
        # ... lógica de depósito ...
        return saldo_atual, extrato_atual
    ```
    **Exemplo de Chamada no `sistema_bancario_v2.py`**:
    ```python
    saldo, extrato = verificacao_deposito(saldo, deposito, extrato)
    ```
    Aqui, `saldo`, `deposito` e `extrato` são passados estritamente pela sua posição.

-   **Função `historico_extrato` (Argumentos por Posição e Nome - Positional-Only e Keyword-Only Arguments)**:
    Esta função é responsável por exibir o extrato e o saldo. Ela demonstra a combinação de ambos os tipos de argumentos. Argumentos antes do `/` são posicionais, e argumentos após o `*` são nomeados.
    ```python
    def historico_extrato(extrato_atual, /, *, saldo_atual):
        # ... lógica do extrato ...
    ```
    **Exemplo de Chamada no `sistema_bancario_v2.py`**:
    ```python
    historico_extrato(extrato, saldo_atual= saldo)
    ```
    `extrato` é passado por posição, enquanto `saldo_atual` é passado por nome.

#### Funções para Novas Funcionalidades (Usuário e Conta Corrente)

-   **Função `cadastro_usuario`**: Gerencia o processo de registro de novos usuários no sistema.
    ```python
    def cadastro_usuario(lista_usuario):
        # ... lógica de cadastro de usuário ...
        return lista_usuario
    ```
    Esta função coleta dados como nome, data de nascimento, CPF e endereço, e os armazena em uma estrutura de dados. Inclui validação para evitar CPFs duplicados.

-   **Função `cadastro_conta_corrente`**: Permite a criação de novas contas correntes e as vincula a um usuário existente.
    ```python
    def cadastro_conta_corrente(lista_usuario, AGENCIA, n_conta):
        # ... lógica de criação de conta corrente ...
        return lista_usuario, n_conta
    ```
    Esta função atribui um número de agência fixo ("0001") e um número de conta sequencial, associando a nova conta ao usuário correto.

### Estruturas de Dados e Listas

A V2 introduz o uso de estruturas de dados mais complexas, como listas aninhadas de dicionários, para gerenciar informações de usuários e suas contas, o que é um avanço significativo em relação à V1.

-   **Lista de Usuários (`lista_usuario`)**: Esta lista é a principal estrutura para armazenar todos os usuários cadastrados. Cada elemento da lista é um dicionário que representa um usuário, e dentro desse dicionário, as informações do usuário são armazenadas.
    ```python
    lista_usuario = [{"jorbson":{"CPF":"12345"}}]
    ```
    **Exemplo de Adição de Novo Usuário**:
    ```python
    novo_usuario = {"nome":nome, "data_de_nascimento":data_de_nascimento, "CPF":cpf, "Endereço":endereço}
    usuario = {nome_de_usuario: novo_usuario}
    lista_usuario.append(usuario)
    ```
    A estrutura permite armazenar detalhes como nome, data de nascimento, CPF e endereço, além de aninhar outras informações, como as contas bancárias do usuário.

-   **Dicionários para Usuários e Contas**: Dicionários são usados para organizar os dados de cada usuário e de cada conta. Isso permite um acesso mais semântico aos dados (ex: `usuario['nome']`, `conta['Agencia']`).
    ```python
    # Dentro do dicionário do usuário, uma lista de dicionários para as contas
    nova_conta = {"Agencia": AGENCIA, "Numero": n_conta}
    # ...
    if "Contas" not in dados_usuario:
      dados_usuario["Contas"] = []
    dados_usuario["Contas"].append(nova_conta)
    ```
    Esta abordagem permite que um usuário tenha múltiplas contas, cada uma com seus próprios detalhes (agência, número), e que essas contas sejam facilmente acessíveis através do perfil do usuário.

### Regras de Negócio da V2 (`Otimizando o Sistema Bancário com Funções Python - Sistema_Bancario_v2`)

A V2 mantém as regras de negócio da V1 para depósito, saque e extrato, mas as implementa através de funções, adicionando as seguintes regras para gerenciamento de usuários e contas:

#### Operações Bancárias (Refatoradas)

As operações de depósito, saque e extrato agora são realizadas através das funções dedicadas, o que melhora a organização e a reutilização do código. As regras de limite de saque, valor máximo por saque, saldo insuficiente e extrato formatado permanecem as mesmas da V1, mas são encapsuladas dentro das respectivas funções.

#### Cadastro de Usuário

-   **CPF Único**: Uma regra de negócio crucial é que não podem existir dois usuários com o mesmo CPF. A função `cadastro_usuario` verifica a existência do CPF na `lista_usuario` antes de permitir um novo cadastro.
    ```python
    # Trecho de código para verificação de CPF duplicado
    for chave_usuario in lista_usuario:
      for chave_informacao in chave_usuario.values(): 
           print(chave_informacao)        
           if "CPF" in chave_informacao and chave_informacao["CPF"] == cpf:
             print("Ja existe usuario com este CPF. ")        
             return lista_usuario
    ```
-   **Formato de Endereço**: O endereço do usuário é armazenado como uma única string formatada, combinando logradouro, número, bairro, cidade e estado.
    ```python
    endereço = str(f"{logradouro}, {nro}- {bairro}- {cidade}/ {estado}")
    ```

#### Criação de Conta Corrente

-   **Agência Fixa**: Todas as contas são criadas com a agência fixa "0001", conforme especificado.
    ```python
    AGENCIA = "0001"
    # ...
    nova_conta = {"Agencia": AGENCIA, "Numero": n_conta}
    ```
-   **Número Sequencial**: O número da conta é gerado sequencialmente, iniciando em 1 e incrementando a cada nova conta criada.
    ```python
    n_conta = 1 # Inicialização
    # ...
    n_conta += 1 # Incremento na função cadastro_conta_corrente
    ```
-   **Vinculação por Usuário**: A conta é vinculada a um usuário existente. A lógica busca o usuário pelo nome de usuário e, se encontrado, adiciona a nova conta à lista de `Contas` dentro do dicionário desse usuário. Um usuário pode ter múltiplas contas, mas uma conta pertence a apenas um usuário.
    ```python
    # Trecho de código para vincular conta ao usuário
    for usuario in lista_usuario:
      if nome_de_usuario in usuario:
          # ...
          dados_usuario = usuario[nome_de_usuario]
          # ...
          if "Contas" not in dados_usuario:
            dados_usuario["Contas"] = []
          dados_usuario["Contas"].append(nova_conta)
    ```

## Como Executar o Projeto

Para executar a V2 do sistema bancário:

1.  Certifique-se de ter o Python (versão 3.x) instalado em sua máquina.
2.  Salve o código fornecido como `sistema_bancario_v2.py`.
3.  Abra um terminal ou prompt de comando.
4.  Navegue até o diretório onde você salvou o arquivo.
5.  Execute o comando:
    ```bash
    python sistema_bancario_v2.py
    ```

O sistema apresentará um menu inicial interativo no console, permitindo que você realize as operações bancárias, cadastre usuários e crie contas.

## Estrutura do Código

O código da V2 (`Otimizando o Sistema Bancário com Funções Python - Sistema_Bancario_v2`) é mais modular e organizado em comparação com a V1. As variáveis de estado do sistema (saldo, extrato, contadores, lista de usuários e número de conta) ainda são globais, mas a lógica operacional está bem encapsulada em funções.

```
.  
├── sistema_bancario_v1.py  # Versão inicial do sistema bancário (opcional, para comparação)
├── sistema_bancario_v2.py  # Versão otimizada com funções e gerenciamento de usuários/contas
└── README_V2.md            # Este arquivo
```

## Contribuições

Este projeto é um exercício de aprendizado e demonstração de evolução em programação Python. Sugestões e melhorias são bem-vindas, sempre alinhadas com os objetivos educacionais do Bootcamp Santander.



