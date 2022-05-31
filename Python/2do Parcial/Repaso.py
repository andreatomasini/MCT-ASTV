'''#comentarios: son notas para su yo del futuro.

hola

#print(mensaje):permite mandar informacion a la pantalla.
print('hola')

print("saludar")

print(5)

print(5+5)

#constantes son datos que no cambian.

dia=6

print(dia)

pie=3.1416

print(pie)

#variables son datos que pueden o NO cambiar.

calificacion=7

print(calificacion)

calificacion=calificacion+2

print(calificacion)

print('hoy es 4 de enero')

#print mas bonito.

print("tu calificacion es ", calificacion)

print("hoy es",dia,"de enero")

print(pie,"es el valor de pi que usaremos")

#operadores matematicos 
# +suma,-resta,*multiplicacion,/division.

a=2
b=3

print(a+b)
print(a-b)
print(a*b)
print(b/a)

print(a+b*b)

#jerarquia de operaciones (parentesis, potencias, multiplicacion, sumas.)

#loop se refiere a cualquier codigo que se pueda repetir o ciclar n numero de veces.

#While:mientras una condicion se ejecuta (o no)se ejecuta todo el codigo de adentro de la misma.



#operadores logicos 
#a>b a es mayor que b 
#a<b a es menor que b 
# a==b a es identica a b

# a==b a es mayor o igual que b
#a<=b a es menor o igul que b.

tomate=2
while(tomate>0):
  print("hay tomate")
  tomate=tomate-1

#identacion= esta nos dice que lines pertenecen a un ciclo o condicion, puede ser un ciclo simple, puede ser un simple espacio o un tab.
  
  # while True es una condicion que pregunta si se puede ejecutar, si respondes que siel codigo funciona.

while True:
  print('hola')'''


#input nospermite ingresar informacion al codigo desde la consola, se debe presionar ENTER una vez que termines.


#nombre es una variable porque puede cambiar si se ejecuta de nevo.
nombre=input()
print("saludos",nombre)

apellido=input("apellido:")
print("saludos mr.",apellido)

edad=input()
print(edad*10)
#input solo recibe STRINGS,necesitas convervirlo si quieres trabajar con numeros.

#int concertir las letras a numeros.
edad=int(input())
print(edad*10)