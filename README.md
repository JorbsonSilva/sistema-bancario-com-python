# Sistema Bancário Simples em Python

## Visão Geral do Projeto

Este projeto implementa um sistema bancário básico em Python, desenvolvido como parte do **Bootcamp Santander 2025 - Back-end com Python**. O principal objetivo foi aplicar e consolidar conceitos fundamentais da linguagem Python em um cenário prático de operações bancárias, como depósito, saque e extrato.

O desenvolvimento ocorreu no **Módulo 2** do bootcamp, que abordou `Operadores e Manipulação de Strings com Python`. Através da construção deste sistema, diversos tópicos essenciais da programação em Python foram explorados e aplicados diretamente no código.

## Conceitos de Python Abordados com Exemplos do Código

Durante a implementação do `sistema_bancario_v1.py`, os seguintes conceitos de Python foram utilizados:

### Tipos de Dados

O projeto faz uso de diferentes tipos de dados para representar as informações do sistema bancário:

-   **`string` (`str`)**: Utilizado para mensagens de menu, histórico de transações e saídas formatadas. 
    Exemplo de definição de menu:
    ```python
    menu = """ \n=======================MENU========================\n                          \nDigite o número correspondente a opção desejada:\n\n(1) Depósito\n(2) Saque\n(3) Extrato\n(4) Sair.   \n                               \n===================================================             \n\n"""
    ```
    Exemplo de concatenação e formatação de extrato:
    ```python
    extrato += str(f"Deposito de R$ {deposito:.2f}\n")
    ```

-   **`int` (inteiro)**: Empregado para valores que representam contagens ou opções de menu.
    Exemplo de inicialização de contador de saques e leitura de opção:
    ```python
    saques_realizados = 0
    opcao = int()
    # ...
    opcao = int(input("Digite uma opção: "))
    ```

-   **`float` (ponto flutuante)**: Essencial para representar valores monetários, permitindo precisão com casas decimais.
    Exemplo de inicialização de variáveis monetárias e leitura de valores:
    ```python
    deposito = float()
    saldo = 0
    # ...
    deposito = float(input("Digite o valor que você quer depositar: R$ "))
    ```

-   **`bool` (booleano)**: Embora não haja variáveis booleanas explícitas no código, a lógica condicional (`if/elif/else`) internamente avalia expressões para `True` ou `False`.

### Estruturas de Controle de Fluxo

As estruturas de controle de fluxo são cruciais para a lógica operacional do sistema:

-   **`if`, `elif`, `else`**: Utilizadas extensivamente para implementar a lógica condicional das operações bancárias e validações.
    Exemplo de verificação de depósito positivo:
    ```python
    if deposito > 0:
        # ...
    else:
        print("Operação falhou, Valor informado fora dos padrões!!!")
    ```
    Exemplo de validação de saque (saldo, limite e quantidade):
    ```python
    if saque <= 500 and saques_realizados != LIMITE_SAQUE and saldo > 0:
        # ...
    elif saque > 500:
        print("Valor do saque acima do permitido")
    elif saque > saldo:
        print("Saldo insuficiente.")
    else:
        print("Numero de saques acima do permitido diariamente.")
    ```

-   **`while`**: Mantém o menu principal em execução contínua, permitindo que o usuário realize múltiplas operações até decidir sair.
    ```python
    while opcao != 4 :
        print(menu)
        opcao = int(input("Digite uma opção: "))
        # ... (lógica das operações)
    else: 
        print("Obrigado por usar nossos servições.")
    ```

-   **`break` / `continue`**: Embora não explicitamente utilizados no `while` principal para interrupção imediata, o fluxo do programa é controlado pelas escolhas do usuário e retornos ao menu, simulando um comportamento de `continue` implícito para novas operações.

### Operadores

Diversos operadores são empregados para realizar cálculos e comparações:

-   **Operadores de Comparação (`<=`, `>=`, `==`, `!=`)**: Utilizados para verificar condições e limites.
    Exemplo de verificação de limite de saque e saques realizados:
    ```python
    if saque <= 500 and saques_realizados != LIMITE_SAQUE and saldo > 0:
        # ...
    ```
    Exemplo de condição de saída do loop:
    ```python
    while opcao != 4 :
        # ...
    ```

-   **Operadores Aritméticos (`+`, `-`)**: Aplicados para atualizar o saldo da conta.
    Exemplo de adição de depósito ao saldo:
    ```python
    saldo += deposito # Sera somado com valor ja existente.
    ```
    Exemplo de subtração de saque do saldo:
    ```python
    saldo -= saque # Será debitado do valor ja existente
    ```

-   **Operadores de Atribuição (`=`)**: Usados para inicializar e atualizar o valor das variáveis.
    Exemplo de inicialização:
    ```python
    saldo = 0
    LIMITE_SAQUE = 3
    ```
    Exemplo de atribuição após cálculo:
    ```python
    saques_realizados += 1
    ```

## Regras de Negócio do Sistema Bancário (v1)

O sistema `sistema_bancario_v1.py` adere estritamente às seguintes regras de negócio:

### Operação de Depósito
-   **Valores Positivos**: Apenas valores maiores que zero são aceitos para depósito.
    ```python
    if deposito > 0:
        # ...
    else:
        print("Operação falhou, Valor informado fora dos padrões!!!")
    ```
-   **Usuário Único**: O sistema não gerencia múltiplos usuários, agências ou contas. Todas as operações afetam um único saldo.
-   **Registro no Extrato**: Cada depósito é registrado no `extrato` com formatação monetária.
    ```python
    extrato += str(f"Deposito de R$ {deposito:.2f}\n")
    ```

### Operação de Saque
-   **Limite Diário**: O usuário pode realizar no máximo `LIMITE_SAQUE` (definido como 3) saques por dia.
    ```python
    LIMITE_SAQUE = 3
    saques_realizados = 0
    # ...
    if saque <= 500 and saques_realizados != LIMITE_SAQUE and saldo > 0:
        saques_realizados += 1
    ```
-   **Limite por Saque**: Cada saque individual não pode exceder `VALOR_MAXIMO_SAQUE` (definido como R$ 500).
    ```python
    VALOR_MAXIMO_SAQUE = 500
    # ...
    if saque <= 500 and saques_realizados != LIMITE_SAQUE and saldo > 0:
        # ...
    elif saque > 500:
        print("Valor do saque acima do permitido")
    ```
-   **Verificação de Saldo**: O saque só é permitido se houver saldo suficiente na conta.
    ```python
    if saque <= 500 and saques_realizados != LIMITE_SAQUE and saldo > 0:
        # ...
    elif saque > saldo:
        print("Saldo insuficiente.")
    ```
-   **Registro no Extrato**: Cada saque é registrado no `extrato` com formatação monetária.
    ```python
    extrato += str(f"Saque de R$ {saque:.2f}\n")
    ```

### Operação de Extrato
-   **Listagem de Transações**: Exibe todas as operações de depósito e saque registradas na variável `extrato`.
    ```python
    print(extrato)
    ```
-   **Saldo Atual**: O saldo final da conta é exibido após a listagem das transações.
    ```python
    print(f"Seu Saldo é R${saldo:.2f}")
    ```
-   **Formato Monetário**: Todos os valores monetários são apresentados no formato `R$ xxx.xx` utilizando f-strings para formatação de ponto flutuante com duas casas decimais.
    ```python
    f"Deposito de R$ {deposito:.2f}\n"
    f"Saque de R$ {saque:.2f}\n"
    f"Seu Saldo é R${saldo:.2f}"
    ```

## Como Executar o Projeto

Para executar este sistema bancário:

1.  Certifique-se de ter o Python (versão 3.x) instalado em sua máquina.
2.  Salve o código fornecido como `sistema_bancario_v1.py`.
3.  Abra um terminal ou prompt de comando.
4.  Navegue até o diretório onde você salvou o arquivo.
5.  Execute o comando:
    ```bash
    python sistema_bancario_v1.py
    ```

O sistema apresentará um menu interativo no console, permitindo que você realize as operações bancárias.

## Estrutura do Código

O código é contido em um único arquivo `sistema_bancario_v1.py`, com variáveis globais para o estado do sistema (saldo, extrato, contadores) e um loop `while` para o menu principal. A lógica de cada operação é tratada por blocos `if/elif`.

```
.  
├── sistema_bancario_v1.py  # Script principal com a lógica do sistema bancário
└── README.md               # Este arquivo
```

## Contribuições

Este projeto serve como um ponto de partida para o aprendizado de Python e sistemas bancários. Sugestões e melhorias são bem-vindas, sempre alinhadas com os objetivos educacionais do Bootcamp Santander.
