class Conta:
  def __init__(self, numero, Cliente):
    self._saldo = float(0)
    self._numeroconta = int(numero)
    self._agencia = str("0001")
    self._cliente = Cliente
    self._historico = Historico()

  def depositar(self, valor: float):
    if valor >= 0:
      self._saldo += valor 
      return True
    return False 

  def saldo(self):
    return self._saldo
  
  def sacar(self, valor: float):
    if self._saldo >= valor:
      self._saldo -= valor
      return True
    return False
  
  @classmethod  
  def nova_conta(cls, numero, Cliente):
    return cls(numero, Cliente)
 
   
class ContaCorrente(Conta):
  def __init__(self, numero, Cliente):
    super().__init__(numero, Cliente)
    self._limitesaque = 3
    self._limite = float (500.0)
    self.saques_realizados = 0

  def limite(self):
    return self._limite
  
  def limite_saque(self):
    return self._limitesaque
  
  def sacar(self, valor: float):
    if valor >= 0:
      if valor <= self._limite:
        if self.saques_realizados < self._limitesaque:  
          if super().sacar(valor):
            self.saques_realizados += 1
            return True
    return False
      

class Cliente:
  def __init__(self, Endereco, Nome_usuario):
    self._endereco = str(Endereco)
    self._nome_usuario = str(Nome_usuario)
    self._contas = []
        
  def realizar_transacao(self):
    pass
    
  def adicionar_conta(self, conta):
    self._contas.append(conta)
    

class PessoaFisica(Cliente):
  def __init__(self, CPF, Nome, Data, Endereco, Nome_usuario):
    super().__init__(Endereco, Nome_usuario)
    self._cpf = str(CPF)
    self._nome = str(Nome)
    self._data_nascimento = (Data)

class Historico:
  def __init__(self):
    self.transacoes = []

  def adicionar_transacao (self, transacao):
    self.transacoes.append(transacao)


from abc import ABC, abstractmethod

class Transacao(ABC):
  @abstractmethod
  def registrar(self, conta):
    pass

class Deposito(Transacao):
  def __init__(self, valor):
    self._valor = float(valor)

  def registrar(self, conta):
    sucesso_deposito = conta.depositar(self._valor) 
    if sucesso_deposito:
      conta._historico.adicionar_transacao(self)
      return True
    return False

class Saque(Transacao):
  def __init__(self, valor):
    self._valor = float(valor)

  def registrar(self, conta):
    sucesso_saque = conta.sacar(self._valor)
    if sucesso_saque:
      conta._historico.adicionar_transacao(self)
      return True
    return False

clientes = [] # objetos Pessoa Fisica 
contas =[]
lista_usuario = []
n_conta = 0 

# Menus interativos

def tela_inicial(): # finalizado
   print("""
===================MENU INICIAL=====================

Seja bem-vindo(a) ao nosso banco digital! Sua jornada
financeira começa agora, de forma simples e segura.
         
(1) Ja sou cliente
(2) Quero me cadastrar    
(9) Sair.                         

Agradecemos por escolher nosso banco digital! 
Sua confiança nos impulsiona a oferecer 
as melhores soluções financeiras.         

====================================================  

""")
   
   opcao = int(input("Digite uma opção: "))

   return opcao

def tela_cliente(cliente_logado): # finalizado
   print(f""" 
=======================MENU========================
Bem vindo, {cliente_logado._nome}                          
Digite o número correspondente a opção desejada:

(1) Selecionar conta corrente
(2) Criar nova conta corrente     
(9) Sair.   
                               
===================================================             

""")
   opcao = int(input("Digite uma opção: "))
   return opcao


def tela_cliente_1(cliente_logado, conta_selecionada): # finalizado
   print(f""" 
=======================MENU========================
Bem vindo, {cliente_logado._nome} 
Conta Corrente: {conta_selecionada._numeroconta}                           
Digite o número correspondente a opção desejada:

(1) Depósito
(2) Saque
(3) Extrato
(9) Sair.   
                               
===================================================             

""")
   opcao = int(input("Digite uma opção: "))
   return opcao

def buscar_cliente(nome_usuario, clientes): # finalizado
  for cliente in clientes:
    if cliente._nome_usuario == nome_usuario:
      return cliente
  print("Nome de usuário não encontrado. Por favor, verifique ou cadastre-se.")
  return None

def buscar_conta_corrente(cliente_logado): # finalizado
  if not cliente_logado._contas: # Verifica se o cliente logado existe uma conta cadastrada
    print("Você não possui contas cadastradas. Por favor, crie uma nova conta.")
    return None
  else:
    print("\nSuas contas disponíveis:")
    for i, conta in enumerate(cliente_logado._contas):
      print(f"{i +1}. Agência:{conta._agencia} - Número da Conta:{conta._numeroconta} - Saldo: R${conta._saldo:.2f}")

    while True:
      escolha = int(input("Digite o número da conta que deseja selecionar (ou 0 para retornar): "))

      if escolha == 0:
        return None
      
      if 1 <= escolha <= len(cliente_logado._contas):
        return cliente_logado._contas[escolha - 1 ]
      else:
        print("Opção de conta inválida. Por favor, digite um número da lista.")

def cadastro_usuario(clientes): # finalizado
  print("""
Olá! Estamos muito felizes por você querer se juntar a nós.
Para começar seu cadastro, siga as instruções e em breve
você terá acesso a todas as nossas funcionalidades.
""")
  
  print("Informe seus dados para o cadastro.")  

  # Criação de usuario
  
  nome_de_usuario = str(input("Digite nome de Usuario: "))
  for usuario_existente in clientes:
    if  usuario_existente._nome_usuario == nome_de_usuario:
      print("Ja existe este usuario.")
      return clientes

  print("Informe seus dados para o cadastro.") 
      
# Coleta de dados do Usuario
  nome = str(input("Digite seu nome: "))
  data_de_nascimento = str(input("Digite sua data de nascimento:\n exp. 00/00/0000 \n"))

  # Verificação de CPF
  cpf = str(input("Digite seu CPF(so números): "))
  for clientes_existente in clientes:
    if clientes_existente._cpf == cpf: 
      print("Ja existe usuario com este CPF. ")        
      return clientes
  # formatação de endereço  
  print("Informe seu Endereço")
  logradouro = str(input("Digite seu logradouro: "))
  nro = str(input("Digite o numero da sua residencia: "))
  bairro = str(input("Digite seu bairro: "))
  cidade = str(input("Digite seu cidade: "))
  estado = str(input("Digite seu estado exp(DF): "))
  endereço = str(f"{logradouro}, {nro}- {bairro}- {cidade}/ {estado}")

  # criação do Objeto 
  novo_cliente = PessoaFisica(CPF = cpf, Nome = nome, Data = data_de_nascimento, Endereco = endereço, Nome_usuario = nome_de_usuario)
  
  clientes.append(novo_cliente)

  return clientes

while True:
   opcao = tela_inicial()
   
   if opcao == 1: 
         
    if not clientes:
      print("Nenhum cliente cadastrado ainda. Por favor, cadastre-se primeiro.")
      continue

    nome_usuario = str(input("Digite Nome de usuario: "))

    cliente_logado = buscar_cliente(nome_usuario, clientes)

    if cliente_logado:
           
      while True:
                              
        opcao_cliente = tela_cliente(cliente_logado)

        if opcao_cliente == 1:

          conta_selecionada = buscar_conta_corrente(cliente_logado)

          if conta_selecionada:           

            while True:     

              opcao_operacao = tela_cliente_1(cliente_logado, conta_selecionada)

              if opcao_operacao == 1: # Depósito
                                             
                valor_deposito = float(input("Digite o valor que você quer depositar: R$ "))
                deposito_obj = Deposito(valor_deposito)

                if deposito_obj.registrar(conta_selecionada):
                  print("Depósito realizado com sucesso!")
                  
                else:
                  print("Falha no Depósito. O Valor deve ser maior que zero.")                  
    
              elif opcao_operacao == 2: # Saque
                                              
                valor_saque = float(input("Digite o valor que voce que Sacar: R$ "))
                saque_obj = Saque(valor_saque)

                if saque_obj.registrar(conta_selecionada):
                  print("Retire seu dinheiro na boca do Caixa.")

                else:
                  print("Valor informado nao diponivel para saque.")
    
              elif opcao_operacao == 3: # Extrato  

                print("\n--------------- EXTRATO ---------------------")   

                if not conta_selecionada._historico.transacoes:
                  print("Não há histórico de transações para esta conta.")
                else:
                  for transacao in conta_selecionada._historico.transacoes:
                    if isinstance(transacao , Deposito):
                      print(f"Depósito: R$ {transacao._valor:.2f}")

                    elif isinstance(transacao , Saque):
                      print(f"Saque: R$ -{transacao._valor:.2f}")

                  print(f"Saldo atual: R${conta_selecionada._saldo:.2f}")
   
              elif opcao_operacao == 9 : 
                print("Obrigado por usar nossos servições.")
                break

              else:
               continue
        
        elif opcao_cliente == 2: # Criar Conta Corrente

            print(f"""
Olá! Que bom ter você {cliente_logado._nome} com a gente.

Para começar a usar nossos serviços, 
siga as instruções e crie sua conta corrente. 
Em breve, você terá acesso a todas 
as nossas funcionalidades e benefícios. 
Se você já tem uma conta corrente, você pode criar outra. 
        
""")
            n_conta += 1

            nova_conta = ContaCorrente.nova_conta(numero=n_conta, Cliente=cliente_logado)
            cliente_logado.adicionar_conta(nova_conta)
            contas.append(nova_conta)

            print(f"Conta corrente {nova_conta._numeroconta} criada com sucesso para {cliente_logado._nome}!")
          
           
        elif opcao_cliente == 9:
          print("Obrigado por usar nossos servições.")
          break
              
   elif opcao == 2: # Cadastrar Usuario
     clientes = cadastro_usuario(clientes)


   elif opcao ==  9:
     break
