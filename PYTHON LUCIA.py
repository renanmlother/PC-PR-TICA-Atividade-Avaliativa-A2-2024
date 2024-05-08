def menu ():
    print (f"Ações disponíveis:")
    print (f"1 - Cadastrar novo funcionário")
    print (f"2 - Excluir funcionário existente")
    print (f"3 - Determinar folha de pagamento de funcionário específico")
    print (f"4 - Determinar relatório de salário bruto e líquido de todos os funcionários")
    print (f"5 - Imprimir dados do funcionário com maior salário")
    print (f"6 - Imprimir dados do funcionário com mais faltas no mês")
    print (f"0 - Encerrar programa")

def cadastrar():
    print(f"Digite as informações do funcionário que deseja cadastrar:\n")

    mat = int(input("Digite a matrícula do funcionário: "))
    nome = input("Digite o nome do funcionário: ")
    cod = int(input("Digite o código da função (101/102): "))
    if cod==101:
        vol = int(input("Digite o volume de vendas mensal do funcionário: "))
        sal = 1500 + vol*0.09
    elif cod == 102:
        sal=int(input("Digite o salário bruto do funcionário"))
    else:
        print("Digite um código válido")
        return
    falta = int(input("Digite o número de faltas do funcionário: "))

    #CONFIRMAÇÃO
    check= input(f"Confirmar cadastro (S/N)?: ")

    if check=='S':
        funcionario = {"matricula": mat, "nome": nome, "codigo": cod, "faltas": falta, "salario": sal}
        funcionarios.append(funcionario)
    else:
        print("Cadastro cancelado")

def excluir():
    matricula = int(input("Digite a matrícula do funcionário que deseja excluir: "))

    for funcionario in funcionarios:
        if funcionario["matricula"] == matricula:
            funcionarios.remove(funcionario)
            print("Funcionário excluído com sucesso.")
            return

    print("Funcionário não encontrado.")

def folha():
    matricula = int(input("Digite a matrícula do funcionário de que deseja determinar a folha de pagamento: "))

    for funcionario in funcionarios:
        if funcionario["matricula"] == matricula:
            salario = funcionario["salario"]
            if salario <= 2259.20:
                percentual_ir = 'Isento'
            elif salario <= 2828.65:
                percentual_ir = '7,5%'
            elif salario <= 3751.05:
                percentual_ir = '15%'
            elif salario <= 4664.68:
                percentual_ir = '22,5%'
            else:
                percentual_ir = '27,5%'

            # Imprimindo informações do funcionário
            print(f"Matrícula: {funcionario['matricula']}")
            print(f"Nome: {funcionario['nome']}")
            print(f"Código da função: {funcionario['codigo']}")
            print(f"Número de faltas: {funcionario['faltas']}")
            print(f"Salário bruto: R$ {funcionario['salario']:.2f}")
            print(f"Percentual do imposto de renda: {percentual_ir}")
            return

    print("Funcionário não encontrado.")

def relatorio():
    for funcionario in funcionarios:
        bruto = funcionario["salario"]
        if bruto <= 2259.20:
            ir = 0
        elif bruto <= 2828.65:
            ir = bruto * 0.075
        elif bruto <= 3751.05:
            ir = bruto * 0.15
        elif bruto <= 4664.68:
            ir = bruto * 0.225
        else:
            ir = bruto * 0.275
        
        if bruto <= 1751.81:
            inss = bruto * 0.08
        elif bruto <= 2919.72:
            inss = bruto * 0.09
        elif bruto <= 5839.45:
            inss = bruto * 0.11
        else:
            inss = 642.34
        
        liquido = bruto - ir - inss

        print(funcionario["matricula"], funcionario["nome"], funcionario["codigo"], "Salário bruto: ", bruto, "Salário líquido: ", liquido, '\n')

#def printmaior():

#def printfalta():

funcionarios = []

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastrar()
    elif opcao == '2':
        excluir()
    elif opcao == '3':
        folha()
    elif opcao == '4':
        relatorio()
    #elif opcao == '5':
    #    printmaior()
    #elif opcao == '6':
    #    printfalta()
    elif opcao == '0':
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")


    
