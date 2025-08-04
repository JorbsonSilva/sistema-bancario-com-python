deposito = float()
saque = float()
saldo = 0
LIMITE_SAQUE = 3
saques_realizados = 0
VALOR_MAXIMO_SAQUE = 500
opcao = int(    )
extrato = str()

# Menus interativos

menu = """ 
=======================MENU========================
                          
Digite o número correspondente a opção desejada:

(1) Depósito
(2) Saque
(3) Extrato
(4) Sair.   
                               
===================================================             

"""

menu_1 = """"
___________________________________________________
Digite o número correspondente a opção desejada:

(5) Retornar ao menu anterior.
(4) Sair.
___________________________________________________
"""

while opcao != 4 :
    print(menu)

    opcao = int(input("Digite uma opção: "))

     # Operação de deposito

    if opcao == 1: 
       
        deposito = float(input("Digite o valor que você quer depositar: R$ "))

         # Verificação se o valor a ser depositado é positivo

        if deposito > 0:        
          extrato += str(f"Deposito de R$ {deposito:.2f}\n") # Armazenamento no historico do extrato o valor depositado
          saldo += deposito # Sera somado com valor ja existente. 
          print(f"O valor do seu deposito foi de R$ {deposito:.2f}")     

          print(menu_1) # Menu secundario
          opcao = int(input("Digite uma opção: "))

        else:
          print("Operação falhou, Valor informado fora dos padrões!!!")   
          print(menu_1) # Menu Secundario
          opcao = int(input("Digite uma opção: "))
                     
      # Operação de Saque               
                    
    elif opcao == 2:
        
        saque = float(input("Digite o valor que voce que Sacar: R$ "))

         # Verificação se existe saldo suficiente e se respeita o Limite de saque e valor maximo de saque.

        if saque <= 500 and saques_realizados != LIMITE_SAQUE and saldo > 0: 
          saques_realizados += 1 # registro o numero de vezes que ja foi realizado o saque.
          saldo -= saque # Será debitado do valor ja existente
          extrato += str(f"Saque de R$ {saque:.2f}\n") # Armazenamento no historico do extrato o valor sacado.          
          print("Retire o dinheiro na boca do caixa !!!")
          
          print(menu_1) # Menu secundario
          opcao = int(input("Digite uma opção: "))
         

        elif saque > 500:
          print("Valor do saque acima do permitido")

          print(menu_1) # Menu secundario
          opcao = int(input("Digite uma opção: "))  

        elif saque > saldo:
          print("Saldo insuficiente.")

          print(menu_1) # Menu secundario
          opcao = int(input("Digite uma opção: ")) 
              
        else :
          print("Numero de saques acima do permitido diariamente.")

          print(menu_1) # Menu secundario
          opcao = int(input("Digite uma opção: ")) 
            
    elif opcao == 3:
        print()
        print("===================================================")
        print("           Historico de transações")
        print()
        print(extrato)
        print(f"Seu Saldo é R${saldo:.2f}")
        print()
        print("===================================================")

else: 
    print("Obrigado por usar nossos servições.")

























