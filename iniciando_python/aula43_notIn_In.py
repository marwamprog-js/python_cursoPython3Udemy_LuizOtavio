nome = 'Otávio'

print(nome[2])
print(nome[-4])

print(10 * '-')

# Se 'á' está ou contém dentro da variavel nome retorne true
print('á' in nome)

# Se 'z' está ou contém dentro da variavel nome retorne true
print('z' in nome)

# Se 'vio' está ou contém dentro da variavel nome retorne true
print('vio' in nome)

print(10 * '-')

# Se 'vio' NÃO está ou contém dentro da variavel nome retorne true
print('vio' not in nome)

# Se 'á' NÃO está ou contém dentro da variavel nome retorne true
print('z' not in nome)


### ---------------
nome = input('Digite seu nome: ')
encontrar = input('Digite uma letra ou para que deseja encontrar no nome informado: ')

if encontrar in nome:
    print(f'"{encontrar}" está em "{nome}"')
else:
    print(f'"{encontrar}" NÃO está em "{nome}"')