
#Calculadora

operação = input('Digite a operação (+, -, *, /) ou = para sair: ')
while operação != '=':
    numero = input('Digite um número: ') 
    numero1 = input('Digite outro número: ')
    if operação == '+':
        print(f'{numero} + {numero1} = {int(numero) + int(numero1)}')
    elif operação == '-':
        print(f'{numero} - {numero1} = {int(numero) - int(numero1)}')
    elif operação == '*':
        print(f'{numero} * {numero1} = {int(numero) * int(numero1)}')
    elif operação == '/':
        print(f'{numero} / {numero1} = {int(numero) / int(numero1)}')
    else:
        print('Operação inválida!')
    
    operação = input('Digite a operação (+, -, *, /) ou = para sair: ')