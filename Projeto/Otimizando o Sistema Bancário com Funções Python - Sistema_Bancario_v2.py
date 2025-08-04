deposito = float()
saque = float()
saldo = 0
LIMITE_SAQUE = 3
saques_realizados = 0
VALOR_MAXIMO_SAQUE = 500
opcao = int(    )
extrato = str()
AGENCIA = "0001"
n_conta = 1
lista_usuario = [{"jorbson":{"CPF":"12345"}}]

# Menus interativos

def tela_inicial():
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

def tela_cliente():
   print(""" 
=======================MENU========================
                          
Digite o número correspondente a opção desejada:

(1) Depósito
(2) Saque
(3) Extrato
(4) Criar nova conta corrente       
(9) Sair.   
                               
===================================================             

""")

def tela_cliente_1():

   print(""""
___________________________________________________
Digite o número correspondente a opção desejada:

(5) Retornar ao menu anterior.
(9) Sair.
___________________________________________________
""")

def cadastro_usuario(lista_usuario):
  print("""
Olá! Estamos muito felizes por você querer se juntar a nós.
Para começar seu cadastro, siga as instruções e em breve
você terá acesso a todas as nossas funcionalidades.
""")
  
  # Criação de usuario
  usuario = {}
  nome_de_usuario = str(input("Digite nome de Usuario: "))
  for chave_usuario in lista_usuario:
    if  nome_de_usuario in chave_usuario:
      print("Ja existe este usuario.")
      return lista_usuario

  print("Informe seus dados para o cadastro.")  
      
# Coleta de dados do Usuario
  nome = str(input("Digite seu nome: "))
  data_de_nascimento = str(input("Digite sua data de nascimento:\n exp. 00/00/0000 \n"))

  # Verificação de CPF
  cpf = str(input("Digite seu CPF(so números): "))
  for chave_usuario in lista_usuario:
    for chave_informacao in chave_usuario.values():             
         if "CPF" in chave_informacao and chave_informacao["CPF"] == cpf:
           print("Ja existe usuario com este CPF. ")        
           return lista_usuario
  # formatação de endereço  
  print("Informe seu Endereço")
  logradouro = str(input("Digite seu logradouro: "))
  nro = str(input("Digite o numero da sua residencia: "))
  bairro = str(input("Digite seu bairro: "))
  cidade = str(input("Digite seu cidade: "))
  estado = str(input("Digite seu estado exp(DF): "))
  endereço = str(f"{logradouro}, {nro}- {bairro}- {cidade}/ {estado}")

  # criação dos dicionarios 
  novo_usuario = {"nome":nome, "data_de_nascimento":data_de_nascimento, "CPF":cpf, "Endereço":endereço}
  usuario = {nome_de_usuario: novo_usuario}

  lista_usuario.append(usuario)

  return lista_usuario



def cadastro_conta_corrente(lista_usuario, AGENCIA, n_conta):
  print("""
Olá! Que bom ter você com a gente.

Para começar a usar nossos serviços, 
siga as instruções e crie sua conta corrente. 
Em breve, você terá acesso a todas 
as nossas funcionalidades e benefícios.
        
""")
  nome_de_usuario = str(input("Informe seu nome de Usuario: "))
  usuario_encontrado = False
  # verificando usuario
  for usuario in lista_usuario:
    if nome_de_usuario in usuario:
        print(f"Usuario {nome_de_usuario} encontrado, criando conta corrente aguarde.")

        dados_usuario = usuario[nome_de_usuario]

        n_conta += 1

        nova_conta = {"Agencia": AGENCIA, "Numero": n_conta}

        if "Contas" not in dados_usuario:
          dados_usuario["Contas"] = []
          
          dados_usuario["Contas"].append(nova_conta)

          print(f"Sua conta é {n_conta}, agencia {AGENCIA}.")

          usuario_encontrado = True

          break
          
        else:
                      
            dados_usuario["Contas"].append(nova_conta)

            print(f"Sua conta é {n_conta}, agencia {AGENCIA}.")

            usuario_encontrado = True

          
  if not usuario_encontrado:
    print("Usuario não encontrado.")

  return lista_usuario, n_conta

      
def verificacao_deposito(saldo_atual, deposito, extrato_atual):
   
   if deposito >= 0:
    extrato_atual += str(f"Deposito de R$ {deposito:.2f}\n") # Armazenamento no historico do extrato o valor depositado
    saldo_atual += deposito # Sera somado com valor ja existente. 
    print(f"O valor do seu deposito foi de R$ {deposito:.2f}") 
    tela_cliente_1() # Menu secundario
    opcao = int(input("Digite uma opção: "))
   else:
    print("Operação falhou, Valor informado fora dos padrões!!!")   
    tela_cliente_1() # Menu Secundario
    opcao = int(input("Digite uma opção: "))

   return saldo_atual, extrato_atual

def verificacao_saque(*, saque, saques_realizados_atual, LIMITE_SAQUE, VALOR_MAXIMO_SAQUE, saldo_atual, extrato_atual):

   if saque <= VALOR_MAXIMO_SAQUE and saques_realizados_atual != LIMITE_SAQUE and saldo_atual > 0: 
    saques_realizados_atual += 1 # registro o numero de vezes que ja foi realizado o saque.
    saldo_atual -= saque # Será debitado do valor ja existente
    extrato_atual += str(f"Saque de R$ {saque:.2f}\n") # Armazenamento no historico do extrato o valor sacado.          
    print("Retire o dinheiro na boca do caixa !!!")
          
    tela_cliente_1() # Menu secundario
    opcao = int(input("Digite uma opção: "))
   elif saque > VALOR_MAXIMO_SAQUE:
    print("Valor do saque acima do permitido")

    tela_cliente_1() # Menu secundario
    opcao = int(input("Digite uma opção: "))  

   elif saque > saldo_atual:
    print("Saldo insuficiente.")

    tela_cliente_1() # Menu secundario
    opcao = int(input("Digite uma opção: ")) 
              
   else :
    print("Numero de saques acima do permitido diariamente.")

    tela_cliente_1() # Menu secundario
    opcao = int(input("Digite uma opção: ")) 

   return saldo_atual, extrato_atual, saques_realizados_atual

def historico_extrato(extrato_atual, /, *, saldo_atual):
   
   print()
   print("===================================================")
   print("           Historico de transações")
   print()
   print(extrato_atual)
   print(f"Seu Saldo é R${saldo_atual:.2f}")
   print()
   print("===================================================")
   
   tela_cliente_1()

while True:
   tela_inicial()
   
   opcao = int(input("Digite uma opção: "))

   if opcao == 1: 
         tela_cliente()

         opcao = int(input("Digite uma opção: "))

         # Operação de deposito

         if opcao == 1: 
       
           deposito = float(input("Digite o valor que você quer depositar: R$ "))

           saldo, extrato = verificacao_deposito(saldo, deposito, extrato)
    
         elif opcao == 2:
        
           saque = float(input("Digite o valor que voce que Sacar: R$ "))

           saldo, extrato, saques_realizados = verificacao_saque(saque= saque, saques_realizados_atual= saques_realizados, LIMITE_SAQUE= LIMITE_SAQUE, VALOR_MAXIMO_SAQUE= VALOR_MAXIMO_SAQUE, saldo_atual= saldo, extrato_atual= extrato)
    
         elif opcao == 3:
           historico_extrato(extrato, saldo_atual= saldo)

         elif opcao == 4:
           lista_usuario, n_conta = cadastro_conta_corrente(lista_usuario, AGENCIA, n_conta)
         
         else: 
           print("Obrigado por usar nossos servições.")
   elif opcao == 2:
     lista_usuario = cadastro_usuario(lista_usuario)
           
   elif opcao == 9:
     print("Obrigado por usar nossos servições.")
     break

