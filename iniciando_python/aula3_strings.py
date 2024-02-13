
# aspa simple
print('Texto teste')
print('Texto "teste"')

# aspas duplas
print("Texto teste")

# escape
print("Texto \"teste\"")

# r
print(r"Texto \"teste\"")

#print( type('teste') )

a = 'AAAA'
b = 'BBBB'
c = 1.1

texto1 = 'a={} b={} c={}'
formato = texto1.format(a, b, c)
print(formato)

texto2 = 'b={1} a={0} c={2:.2f}'
formato = texto2.format(a, b, c)
print(formato)


texto3 = 'c={nome3:.2f} b={nome2} a={nome1}'
formato = texto3.format(nome1=a, nome2=b, nome3=c)
print(formato)