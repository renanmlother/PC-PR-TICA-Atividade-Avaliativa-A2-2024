def verificacod(cod):
    global salfixo,vol,salbruto

    while cod!=101 and cod!=102:
        print("Digite um código válido")
        cod = int(input("Digite o código da função (101/102): "))

    if cod==101:
        salfixo = 1500
        vol = float(input("Digite o volume de vendas mensal do funcionário: "))
        salbruto = 1500 + vol*0.09

    else:
        salbruto=int(input("Digite o salário bruto do funcionário: "))
        salfixo = salbruto

    return salbruto,salfixo


def percentual(salbruto):
    if salbruto <= 2259.20:
        percentual_ir = 'Isento'

    elif salbruto <= 2828.65:
        percentual_ir = 7.5

    elif salbruto <= 3751.05:
        percentual_ir = 15

    elif salbruto <= 4664.68:
        percentual_ir = 22.5

    else:
        percentual_ir = 27.5

    if percentual_ir=='Isento':
        print("Funcionário isento de imposto!")
        salliquido=salbruto
    
    else:
        salliquido = salbruto - salbruto*percentual_ir/100

    return salliquido,percentual_ir

def menu ():
    print (f"\nAções disponíveis:")
    print (f"\n1 - Cadastrar novo funcionário")
    print (f"2 - Excluir funcionário existente")
    print (f"3 - Determinar folha de pagamento de funcionário específico")
    print (f"4 - Determinar relatório de salário bruto e líquido de todos os funcionários")
    print (f"5 - Imprimir dados do funcionário com maior salário")
    print (f"6 - Imprimir dados do funcionário com mais faltas no mês")
    print (f"0 - Encerrar programa")

def cadastrar():
    global funcionarios
    salliquido = 0
    aux = []
    salbruto = 0
    global salfixo  
   
    print(f"Digite as informações do funcionário que deseja cadastrar:\n")

    mat = int(input("Digite a matrícula do funcionário: "))
    
    while mat in funcionario.keys():
        print("O código de matrícula já está inserido!")
        mat = int(input("Digite a matrícula do funcionário: "))
    
    nome = input("Digite o nome do funcionário: ")

    cod = int(input("Digite o código da função (101/102): "))
    salbruto, salliquido = verificacod(cod)

    falta = int(input("Digite o número de faltas do funcionário: "))
    while falta>31 and falta<0:
        print("Digite um número valido de faltas!")
        falta = int(input("Digite o número de faltas do funcionário: "))

    if falta==0:
        salbruto = salbruto

    else:
        salbruto = salbruto-(falta*salfixo/30)    

    salliquido,percentual_ir = percentual(salbruto)
    
    #CONFIRMAÇÃO
   
    check= str(input(f"Confirmar cadastro (S/N)?: "))

    check =check.replace(" ","")
    while check.lower()!='s' and check.lower()!='n':
        print("Digite sim ou não! (S ou N)")
        check= str(input(f"Confirmar cadastro (S/N)?: "))

    if check.lower()=='s':
        funcionarios.append(nome)
        funcionarios.append(cod)
        funcionarios.append(falta)
        funcionarios.append(salbruto)
        funcionarios.append(percentual_ir)
        funcionarios.append(salliquido)

        aux = funcionarios.copy()
        funcionario[mat]=aux
        funcionarios.clear()

        print("Cadastro efetuado com sucesso!")
        
    else:
        print("Cadastro cancelado")
        
    print(mat, end = '')
    print(funcionario[mat])


def excluir():

    matricula = int(input("Digite a matrícula do funcionário que deseja excluir: "))

    for k in funcionario.keys():
        if k==matricula:
            del funcionario[k]
            print("Funcionário excluído com sucesso.")
            return

    print("Funcionário não encontrado.")

def folha():
    matricula = int(input("Digite a matrícula do funcionário de que deseja determinar a folha de pagamento: "))

    for k,i in funcionario.items():
        if  k==matricula:
            print(f"\nk",end = '')
            print(i[0:3])
            print(f"Percentual de imposto: {funcionario[matricula][4]}")
            return
    print("Funcionário não encontrado.")

def relatorio():
    for k,i in funcionario.items():
        print(f"\n{k}",end = '')
        print(i[0:3])
        print(f"Sálario bruto: {i[3]},sálario líquido: {i[5]}")
        
def printmaior():
    maior = 0
    global salfixo
    for k,i in funcionario.items():
        if i[5]>maior:
            maior = k
    print(f"\n{maior}",end= '')
    print(funcionario[maior])

def printfalta():
    maior = 0
    for k,i in funcionario.items():
        if i[2]>maior:
            maior = k
    for k,i in funcionario.items():
        if k==maior:
            print(f"\n{maior}",end ="")
            print(funcionario[maior])
            print(f"Seu desconto foi de: {i[2]*salfixo/30}")

funcionarios = []
funcionario = {}


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
    elif opcao == '5':
       printmaior()
    elif opcao == '6':
        printfalta()
    elif opcao == '0':
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")


    

