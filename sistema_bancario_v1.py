menu = ''' 
####################################
# Escolha uma das opções a seguir: #
# [d] Depositar                    #
# [s] Sacar                        #
# [e] Extrato                      #
# [q] Sair                         #
####################################
'''

agradecimento = '''
#####################################################
# Obrigado por usar nosso aplicativo. Volte sempre! #
#####################################################

'''
saldo = 0
limite = 500
extrato = f"Saldo atual: R$ {saldo:.2f} "
numero_saque = 0
limite_saques = 0
operacoes = []

while True:

    opcao = input(menu)

    if  opcao == 'd':
        print('##### Deposito #######')
        valor = float(input("Digite o valor que será depositado: "))
        if valor < 0:
            print('\n ### Digite um valor válido! ### \n')
        else:
            operacoes.append(['Deposito',valor])
            saldo += valor
            #print(f'Saldo atual: R$ {saldo:.2f}')
    
    elif opcao == 's':
        print('##### Saque #####')
        if limite_saques >= 3:
            print('\n### Limite diário de saque excedido! Tente novamente amanhã! ###\n')
        else:
            valor = float(input('Digite o valor que deseja sacar: '))
            if valor > limite:
                print('\n### Valor excede limite máximo de saque. ###\n')
            elif valor < 0:
                print('\n### Digite um valor válido para realizar o saque! ###\n')
            else:
                if valor > saldo:
                    print('\n### Saldo insuficiente! Tente novamente! ###\n')
                else:
                    operacoes.append(['Saque',valor])
                    saldo -= valor
                    limite_saques += 1
                
    elif opcao == 'e':
        print('##### Extrato #####')
        for i in range(0,len(operacoes)):
            print(f'{i+1}: {operacoes[i][0]} --> {operacoes[i][1]}')
        print(f'Saldo atual: {saldo:.2f}')
    
    elif opcao == 'q':
        print(agradecimento)
        break

    else:
        print('\n ### Opção inválida! Selecione um comando válido a partir do menu. ### \n')


    

    