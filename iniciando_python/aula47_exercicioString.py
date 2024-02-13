"""
Exercicio
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade

Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é 
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é 
        A última letra do seu nome é
se nada for digitado em nome ou idade:
    Exiba:
        Desculpe, você deixou campos vazios
        
"""

print("------ BEM VINDO -------")
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome and idade:
    print("\n------ DADOS -------")
    print(f'Seu nome é {nome}')
    #print(f'Seu nome invertido é {nome[-1:-(len(nome) + 1):-1]}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome CONTÉM espaços')
    else:
        print('Seu nome NÃO CONTÉM espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é "{nome[0]}"')
    print(f'A última letra do seu nome é "{nome[(len(nome) - 1)]}"')
    print("----------------------\n\n")
else:
    print("\nDesculpe, você deixou campos vazios")

