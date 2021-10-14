# Listas
nombre = 'Paulina'
print(nombre[0])
nombres = ['Paulina', 'Moises', 'Hector', 'Balam', 'Raúl', 'Jocelyn']
print(nombres)

nombres[0] = 'Max'
print(nombres)

nombres.sort()
print(nombres)

nombres.append('Paulina')
nombres.reverse()
print(nombres)

# Tuplas
tupla = (1, 2, 3, 4, 5, 3, 5)

print(tupla)
print(tupla.count(3))
print(tupla.index(3))
#tupla[0] = 23

# Set
#https://docs.python.org/3/tutorial/datastructures.html#sets
s = set()

s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)

print(s)

s.remove(3)

print(s)

s.add(2)
s.add(2)
s.add(2)

print(s)

# Diccionario
edades = {'Paulina':21, 'Moises':22, 'Hector':23, 'Balam':24,
           'Raúl':25, 'Jocelyn':26}

print(edades)

print(edades['Jocelyn'])

edades['Raúl'] = 20
print(edades)

edades['Balam'] += 1
print(edades)


# Listas (arreglos) - Secuencia mutable de variables
# Tuplas - Secuencia no mutable de variables
# Set - Colección de valores únicos
# Diccionarios - Colección de pares llave-valor



# Matrices

m = [[1,2,3], [4,5,6]]
print(m)

print(m[0][2])
