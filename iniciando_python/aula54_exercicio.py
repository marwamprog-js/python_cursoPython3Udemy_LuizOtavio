"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

exercicio_exec = input("Informe o número do exercicio: ")
exercicio_exec = int(exercicio_exec)

if exercicio_exec == 1:
    print('------ BEM VINDO -----')
    numero = input('Favor digite um número inteiro: ')

    try:
        numero = int(numero)

        if numero % 2 == 0:
            print(f'O número {numero} digitado é PAR')
        else:
            print(f'O número {numero} digitado é IMPAR')
    except ValueError:
        print(f'O valor informado "{numero}" não é um número inteiro')




"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

if exercicio_exec == 2:
    print('----- Bem vindo -----')
    hora = input("Informe a Hora: ")

    #print(hora)
    try:
        hora = int(hora)

        if hora >= 0 and hora <= 11:
            print("Bom dia")
        elif hora > 11 and hora <= 17:
            print("Boa tarde")
        elif hora > 17 and hora <= 23:
            print("Boa noite")
        else:
            print("Valor informado não é um horario")    
    except ValueError:
        print("Valor informado inválido")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""


if exercicio_exec == 3:
    print('----- Bem vindo -----')
    nome = input("Informe seu nome: ")

    if nome != "":
        if len(nome) <= 4:
            print("Seu nome é curto")
        elif len(nome) > 4 and len(nome) <= 6:
            print("Seu nome é normal")    
        else:
            print("Seu nome é muito grande")    
    else:
        print("Programa finalizado. Você não informou nenhum nome.")