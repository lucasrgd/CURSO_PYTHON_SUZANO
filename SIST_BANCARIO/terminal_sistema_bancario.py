menu = """
# SISTEMA BANCARIO

[d] Depositar
[e] Extrato
[s] Sacar
[q] Sair

=> """
# Variáveis
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

# Funções
while True:
    opcao = input(menu)
    
    if opcao == "d":
       valor = float(input("INFORME O VALOR DO DEPÓSITO: ")) 
       if valor > 0:
           saldo += valor
           extrato += f"Depósito: R$ {valor:.2f}\n"
           
       else:
           print("OPERAÇÃO SEM SUCESSO! VALOR INVÁLIDO.") 
    
    elif opcao == "s":
        valor = float(input("INFORME O VALOR DO SAQUE: "))
        
        excedeu_saque = valor > saldo
        
        excedeu_limite = valor > limite 
        
        excedeu_saques = numero_saques >= limite_saques
        
        if excedeu_saque:
            print("OPERAÇÃO SEM SUCESSO! SALDO INSUFICIENTE.")
        elif excedeu_limite:
            print("OPERAÇÃO SEM SUCESSO! LIMITE EXCEDIDO.")
        elif excedeu_saques:
            print("OPERAÇÃO SEM SUCESSO! LIMITE DE SAQUES EXCEDIDO.")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("OPERAÇÃO SEM SUCESSO! VALOR INVÁLIDO.")
    
    elif opcao == "e":
        print("\n==================== EXTRATO ====================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================================================")
        
        
    elif opcao == "q":
        print("Saindo...")
        break
    
    else:
        print("Opção inválida!")