# Sistema Bancário Orientado a Objetos (V3)

## Visão Geral do Projeto

Este documento detalha a **Versão 3 (V3)** do sistema bancário, desenvolvida como parte do **Bootcamp Santander 2025 - Back-end com Python**. Esta versão representa uma evolução significativa em relação às anteriores (V1 e V2), com foco na implementação de um modelo de classes orientado a objetos, conforme o diagrama UML fornecido.

O principal objetivo da V3 foi refatorar o sistema para armazenar dados de clientes e contas bancárias em objetos, em vez de dicionários, e atualizar os métodos que tratam as opções do menu para funcionarem com as classes modeladas. Isso resulta em um código mais robusto, escalável e alinhado com os princípios de Programação Orientada a Objetos (POO).




## Contexto do Desenvolvimento

A V3 do sistema bancário foi desenvolvida com base nos conhecimentos de **Programação Orientada a Objetos (POO)**. Ela aprimora a estrutura da V2, que introduziu funções e dicionários, ao substituir a representação de dados por classes e objetos. Esta refatoração visa melhorar a organização, a manutenção e a escalabilidade do código, seguindo um design mais formal e modular.




## Objetivo Geral da V3

O principal objetivo da V3 é refatorar o sistema bancário para utilizar um modelo de classes orientado a objetos, conforme o diagrama UML fornecido. Isso inclui:

-   **Armazenamento de Dados em Objetos**: Clientes e contas bancárias são agora representados por instâncias de classes, em vez de dicionários.
-   **Atualização dos Métodos**: Os métodos que tratam as opções do menu foram adaptados para interagir com os novos objetos e suas propriedades.
-   **Implementação de Herança e Polimorfismo**: Utilização de herança para `ContaCorrente` (que herda de `Conta`) e `PessoaFisica` (que herda de `Cliente`), e polimorfismo com a interface `Transacao` para `Deposito` e `Saque`.




## Conceitos de Python Abordados na V3 com Exemplos do Código (`Modelando o Sistema Bancário em POO com Python - Sistema_Bancario_v3`)

Esta seção detalha os conceitos de Python aplicados na V3, com exemplos diretos do arquivo `Modelando o Sistema Bancário em POO com Python - Sistema_Bancario_v3`, com foco na Programação Orientada a Objetos (POO).

### Classes e Objetos

A V3 refatora completamente a forma como os dados são estruturados, utilizando classes para modelar as entidades do sistema bancário:

-   **`Conta`**: Classe base para as contas bancárias, com atributos como `_saldo`, `_numeroconta`, `_agencia`, `_cliente` e `_historico`. Inclui métodos para `depositar`, `saldo` e `sacar`.
    ```python
    class Conta:
      def __init__(self, numero, Cliente):
        self._saldo = float(0)
        self._numeroconta = int(numero)
        self._agencia = str("0001")
        self._cliente = Cliente
        self._historico = Historico()

      def depositar(self, valor: float):
        # ...
    ```

-   **`ContaCorrente`**: Herda de `Conta`, adicionando atributos específicos como `_limitesaque` e `_limite`, e sobrescrevendo o método `sacar` para incluir a lógica de limite de saques.
    ```python
    class ContaCorrente(Conta):
      def __init__(self, numero, Cliente):
        super().__init__(numero, Cliente)
        self._limitesaque = 3
        self._limite = float (500.0)
        self.saques_realizados = 0

      def sacar(self, valor: float):
        # ...
    ```

-   **`Cliente`**: Classe base para os clientes, com atributos como `_endereco`, `_nome_usuario` e `_contas`. Inclui métodos para `realizar_transacao` e `adicionar_conta`.
    ```python
    class Cliente:
      def __init__(self, Endereco, Nome_usuario):
        self._endereco = str(Endereco)
        self._nome_usuario = str(Nome_usuario)
        self._contas = []
            
      def adicionar_conta(self, conta):
        self._contas.append(conta)
    ```

-   **`PessoaFisica`**: Herda de `Cliente`, adicionando atributos específicos para pessoas físicas como `_cpf`, `_nome` e `_data_nascimento`.
    ```python
    class PessoaFisica(Cliente):
      def __init__(self, CPF, Nome, Data, Endereco, Nome_usuario):
        super().__init__(Endereco, Nome_usuario)
        self._cpf = str(CPF)
        self._nome = str(Nome)
        self._data_nascimento = (Data)
    ```

-   **`Historico`**: Classe para registrar as transações de uma conta, contendo uma lista de `transacoes` e o método `adicionar_transacao`.
    ```python
    class Historico:
      def __init__(self):
        self.transacoes = []

      def adicionar_transacao (self, transacao):
        self.transacoes.append(transacao)
    ```

### Abstração e Polimorfismo

A V3 introduz o conceito de abstração e polimorfismo através da classe abstrata `Transacao` e suas implementações concretas:

-   **`Transacao` (Classe Abstrata)**: Define uma interface comum para todas as transações, com o método abstrato `registrar`.
    ```python
    from abc import ABC, abstractmethod

    class Transacao(ABC):
      @abstractmethod
      def registrar(self, conta):
        pass
    ```

-   **`Deposito`**: Implementa a classe `Transacao`, registrando um depósito na conta.
    ```python
    class Deposito(Transacao):
      def __init__(self, valor):
        self._valor = float(valor)

      def registrar(self, conta):
        sucesso_deposito = conta.depositar(self._valor) 
        if sucesso_deposito:
          conta._historico.adicionar_transacao(self)
          return True
        return False
    ```

-   **`Saque`**: Implementa a classe `Transacao`, registrando um saque na conta.
    ```python
    class Saque(Transacao):
      def __init__(self, valor):
        self._valor = float(valor)

      def registrar(self, conta):
        sucesso_saque = conta.sacar(self._valor)
        if sucesso_saque:
          conta._historico.adicionar_transacao(self)
          return True
        return False
    ```

### Interação com o Usuário e Gerenciamento de Objetos

As funções de interação com o usuário (`tela_inicial`, `tela_cliente`, `tela_cliente_1`, `buscar_cliente`, `buscar_conta_corrente`, `cadastro_usuario`) foram atualizadas para manipular objetos das classes `PessoaFisica`, `ContaCorrente`, `Deposito` e `Saque`, garantindo que todas as operações sejam realizadas através da interface orientada a objetos.




## Regras de Negócio da V3 (`sistema_bancario_v3.py`)

A V3 mantém as regras de negócio das versões anteriores, mas as implementa e gerencia de forma mais coesa e escalável através do modelo de classes:

### Operações Bancárias (Orientadas a Objetos)

-   **Depósito**: A lógica de depósito é encapsulada no método `depositar` da classe `Conta`. A transação é registrada através da classe `Deposito`, que interage com o método `depositar` da conta e adiciona a transação ao histórico.
    ```python
    # Na classe Conta
    def depositar(self, valor: float):
      if valor >= 0:
        self._saldo += valor 
        return True
      return False

    # Na classe Deposito
    def registrar(self, conta):
      sucesso_deposito = conta.depositar(self._valor) 
      if sucesso_deposito:
        conta._historico.adicionar_transacao(self)
        return True
      return False
    ```

-   **Saque**: A lógica de saque é tratada no método `sacar` da classe `Conta` e sobrescrita na `ContaCorrente` para incluir as regras de limite. A transação é registrada através da classe `Saque`, que interage com o método `sacar` da conta e adiciona a transação ao histórico.
    -   **Limite Diário e por Saque**: Gerenciados pelos atributos `_limitesaque` e `_limite` na `ContaCorrente` e verificados no método `sacar`.
    -   **Verificação de Saldo**: Realizada no método `sacar` da classe `Conta`.
    ```python
    # Na classe ContaCorrente (sobrescrevendo o método sacar da Conta)
    def sacar(self, valor: float):
      if valor >= 0:
        if valor <= self._limite:
          if self.saques_realizados < self._limitesaque:  
            if super().sacar(valor):
              self.saques_realizados += 1
              return True
      return False

    # Na classe Saque
    def registrar(self, conta):
      sucesso_saque = conta.sacar(self._valor)
      if sucesso_saque:
        conta._historico.adicionar_transacao(self)
        return True
      return False
    ```

-   **Extrato**: O histórico de transações é armazenado no objeto `Historico` associado a cada `Conta`. O extrato é gerado iterando sobre as transações registradas no histórico e exibindo os detalhes de cada `Deposito` ou `Saque`.
    ```python
    # No loop principal, ao exibir o extrato
    if not conta_selecionada._historico.transacoes:
      print("Não há histórico de transações para esta conta.")
    else:
      for transacao in conta_selecionada._historico.transacoes:
        if isinstance(transacao , Deposito):
          print(f"Depósito: R$ {transacao._valor:.2f}")
        elif isinstance(transacao , Saque):
          print(f"Saque: R$ -{transacao._valor:.2f}")
      print(f"Saldo atual: R${conta_selecionada._saldo:.2f}")
    ```

### Gerenciamento de Clientes e Contas

-   **Cadastro de Usuário**: A função `cadastro_usuario` cria instâncias da classe `PessoaFisica`, garantindo que o CPF e o nome de usuário sejam únicos antes de adicionar o novo cliente à lista global `clientes`.
    ```python
    # Trecho da função cadastro_usuario
    novo_cliente = PessoaFisica(CPF = cpf, Nome = nome, Data = data_de_nascimento, Endereco = endereço, Nome_usuario = nome_de_usuario)
    clientes.append(novo_cliente)
    ```

-   **Criação de Conta Corrente**: A função de criação de conta agora instancia `ContaCorrente` e a associa ao objeto `Cliente` logado, adicionando a nova conta à lista `_contas` do cliente e à lista global `contas`.
    -   **Agência Fixa**: Definida como "0001" no construtor da classe `Conta`.
    -   **Número Sequencial**: Gerado globalmente e atribuído ao criar uma nova `ContaCorrente`.
    -   **Vinculação por Cliente**: A conta é diretamente vinculada ao objeto `Cliente` no momento da criação.
    ```python
    # Trecho do loop principal para criar conta
    nova_conta = ContaCorrente.nova_conta(numero=n_conta, Cliente=cliente_logado)
    cliente_logado.adicionar_conta(nova_conta)
    contas.append(nova_conta)
    ```




## Como Executar o Projeto

Para executar a V3 do sistema bancário:

1.  Certifique-se de ter o Python (versão 3.x) instalado em sua máquina.
2.  Salve o código fornecido como `Modelando o Sistema Bancário em POO com Python - Sistema_Bancario_v3`.
3.  Abra um terminal ou prompt de comando.
4.  Navegue até o diretório onde você salvou o arquivo.
5.  Execute o comando:
    ```bash
    python Modelando o Sistema Bancário em POO com Python - Sistema_Bancario_v3
    ```

O sistema apresentará um menu inicial interativo no console, permitindo que você realize as operações bancárias, cadastre usuários e crie contas, tudo gerenciado por objetos.




## Estrutura do Código

O código da V3 (`Modelando o Sistema Bancário em POO com Python - Sistema_Bancario_v3`) é estruturado em classes que representam as entidades do domínio bancário, seguindo o diagrama UML. As interações são realizadas através de métodos dessas classes, e o fluxo principal do programa coordena as chamadas a esses métodos e a manipulação dos objetos.

```
.  
├── sistema_bancario_v1.py  # Versão inicial do sistema bancário (para comparação)
├── sistema_bancario_v2.py  # Versão otimizada com funções e gerenciamento de usuários/contas (para comparação)
├── sistema_bancario_v3.py  # Versão orientada a objetos
├── README.V1.md            # README da versão 1
├── README_V2.md            # README da versão 2
└── README_V3.md            # Este arquivo
```




## Contribuições

Este projeto é um exercício de aprendizado e demonstração de evolução em programação Python, com foco em Programação Orientada a Objetos. Sugestões e melhorias são bem-vindas, sempre alinhadas com os objetivos educacionais do Bootcamp Santander.

