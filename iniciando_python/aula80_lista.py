"""
Tipo list - Mutável

Métodos úteis:
    append, insert, pop, del, clear, extend, Create Read Update Delete 
"""

lista = [123, True, 'Luiz', 1.2, []]
# print(lista, type(lista))

print(lista)
print(lista[0])

lista[1] = 'Maria'
print(lista)

del lista[2]
print(lista)

# Adicionar valores ao final da lista
lista.append(50)

# Remove o ultimo elemento
lista.pop()

lista.append(60)
lista.append(70)
lista.append('Flavia')

# Remove o ultimo item da lista e atribui a variavel
nome = lista.pop()

# Remove o ultimo item da lista
del lista[-1]

# Adiona item na lista escolhendo uma posicao
lista.insert(0, 'Novo valor')


print(lista)