"""
Fatiamento [i:f:p] [::] 
i = inicio
f = fim
p = parte
"""

variavel = 'Olá mundo'

# pegar a partir da posição 4 até o final 
print(variavel[4:])

# pegar a partir da posição 4 até a posicao 7 
print(variavel[4:8])

# pegar a partir da posição 0 até a posicao 9 pulando de 2 em 2 
print(variavel[0:9:2])

# pegar INVERTIDO a partir da posição -1 até a posicao -10 pulando de -1 em -1 
print(variavel[-1:-10:-1])

# função len() pega o tamanho da variavel
print(len(variavel))