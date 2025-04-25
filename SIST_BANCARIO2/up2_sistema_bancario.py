import json

# Função para salvar os dados
def salvar_dados(lista_usuarios, lista_contas):
    dados = {"usuarios": lista_usuarios, "contas": lista_contas}
    with open("dados_banco.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

# Função para carregar os dados
def carregar_dados():
    try:
        with open("dados_banco.json", "r") as arquivo:
            dados = json.load(arquivo)
            return dados["usuarios"], dados["contas"]
    except FileNotFoundError:
        return [], []

# Carregar dados ao iniciar
lista_usuarios, lista_contas = carregar_dados()

# Função de criação de conta com saldo vinculado
def criar_conta(lista_usuarios, lista_contas):
    cpf = input("Informe o CPF do titular: ")
    usuario = next((usuario for usuario in lista_usuarios if usuario["cpf"] == cpf), None)

    if not usuario:
        print("Usuário não encontrado! Certifique-se de que o CPF está correto ou cadastre o usuário primeiro.")
        return

    numero_conta = len(lista_contas) + 1
    lista_contas.append({"numero_conta": numero_conta, "cpf": cpf, "saldo": 0, "extrato": []})
    print(f"Conta criada com sucesso! Número da conta: {numero_conta}")
    salvar_dados(lista_usuarios, lista_contas)

# Listar contas
def listar_contas(lista_contas):
    if not lista_contas:
        print("Nenhuma conta cadastrada ainda.")
        return

    print("\n======= LISTA DE CONTAS =======")
    for conta in lista_contas:
        print(f"Número da Conta: {conta['numero_conta']}, CPF do Titular: {conta['cpf']}, Saldo: R$ {conta['saldo']:.2f}")
    print("================================")

# Função de depósito vinculado à conta
def depositar(lista_contas):
    numero_conta = int(input("Informe o número da conta para depósito: "))
    conta = next((conta for conta in lista_contas if conta["numero_conta"] == numero_conta), None)

    if not conta:
        print("Conta não encontrada.")
        return

    valor = float(input("Informe o valor do depósito: R$ "))
    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"].append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito realizado com sucesso! Saldo atual: R$ {conta['saldo']:.2f}")
        salvar_dados(lista_usuarios, lista_contas)
    else:
        print("Operação falhou! O valor informado é inválido.")

# Função de saque vinculado à conta
def sacar(lista_contas):
    numero_conta = int(input("Informe o número da conta para saque: "))
    conta = next((conta for conta in lista_contas if conta["numero_conta"] == numero_conta), None)

    if not conta:
        print("Conta não encontrada.")
        return

    valor = float(input("Informe o valor do saque: R$ "))
    if valor > conta["saldo"]:
        print("Operação falhou! Saldo insuficiente.")
    elif valor > 0:
        conta["saldo"] -= valor
        conta["extrato"].append(f"Saque: R$ {valor:.2f}")
        print(f"Saque realizado com sucesso! Saldo atual: R$ {conta['saldo']:.2f}")
        salvar_dados(lista_usuarios, lista_contas)
    else:
        print("Operação falhou! Valor inválido.")

# Função de extrato para exibir as movimentações
def exibir_extrato(lista_contas):
    numero_conta = int(input("Informe o número da conta para consultar o extrato: "))
    conta = next((conta for conta in lista_contas if conta["numero_conta"] == numero_conta), None)

    if not conta:
        print("Conta não encontrada.")
        return

    print("\n======= EXTRATO DA CONTA =======")
    if not conta["extrato"]:
        print("Não foram realizadas movimentações.")
    else:
        for transacao in conta["extrato"]:
            print(transacao)
    print(f"\nSaldo atual: R$ {conta['saldo']:.2f}")
    print("=================================")

# Cadastro de usuários
def cadastrar_usuario(lista_usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario_existente = next((usuario for usuario in lista_usuarios if usuario["cpf"] == cpf), None)

    if usuario_existente:
        print("Usuário já cadastrado.")
        return None

    nome_usuario = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/uf): ")

    lista_usuarios.append({
        "nome": nome_usuario,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    })
    print("Usuário cadastrado com sucesso.")
    salvar_dados(lista_usuarios, lista_contas)
    return nome_usuario

# Menu
menu = """
[u] CADASTRAR-SE
[c] CRIAR CONTA
[l] LISTAR CONTAS
[d] DEPOSITAR
[s] SAQUE
[e] EXTRATO
[q] SAIR

=> """

# Execução do sistema
nome_usuario = None
while True:
    if not nome_usuario:
        print("Bem-vindo(a) ao sistema bancário!")
        print("Caso não tenha cadastro, digite 'u' para cadastrar-se.")

    opcao = input(menu).strip().lower()

    if opcao == "u":
        nome_usuario = cadastrar_usuario(lista_usuarios) or nome_usuario

    elif opcao == "c":
        criar_conta(lista_usuarios, lista_contas)

    elif opcao == "l":
        listar_contas(lista_contas)

    elif opcao == "d":
        depositar(lista_contas)

    elif opcao == "s":
        sacar(lista_contas)

    elif opcao == "e":
        exibir_extrato(lista_contas)

    elif opcao == "q":
        print("Saindo do sistema...")
        salvar_dados(lista_usuarios, lista_contas)
        break

    else:
        print("Opção inválida! Por favor, escolha uma opção válida do menu.")