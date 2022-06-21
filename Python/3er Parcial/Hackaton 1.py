while True:
 print("MENU AL CLIENTE")
 print("Reporte de fallas(seleccione 1)")
 print("Opcion a pago(seleccione 2)")
 print("Promocionessele(seleccione 3)")
 z=(input("Seleccione número:"))
 if z=="1":
  import random

  base="1234567890"


  passw=""
  for i in range(10):
   passw=passw+random.choice(base)
 
  print("Numero de reporte:", passw)
  input()
 if z=="2":
  A=input("Ingresa número de tarjeta(escribelo sin espacios con 16 digitos):\n")
  x=len(A)
  if x==16:
    print("El numero de targjetaes correcto")
    input()
  else:
   print("Ese numero de targjeta o existe")
   input()
 if z=="3":
  print("Telefono iphone gratis!!!")
  input()




