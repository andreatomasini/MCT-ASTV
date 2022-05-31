#5 articulos
#Nombre de artuculo
#Sub total
#Con iva
#Total
#Nombre del cajero
print("Welcome")
n1=(input("Enter the name of the first item:"))
p1=float(input("Enter the price of the first item:"))
n2=(input("Enter the name of the second item:"))
p2=float(input("Enter the price of the second item:"))
n3=(input("Enter the name of the third item:"))
p3=float(input("Enter the price of the third item:"))
n4=(input("Enter the name of the fourth item:"))
p4=float(input("Enter the price of the fourth item:"))
n5=(input("Enter the name of the fifth item:"))
p5=float(input("Enter the price of the fifth item:"))
noIVA=p1+p2+p3+p4+p5
name=input("Write your name:")
print("Cashier:",name)
print(n1)
print("price is=",p1)
print(n2)
print("price is=",p2)
print(n3)
print("price is=",p3)
print(n4)
print("price is=",p4)
print(n5)
print("price is=",p5)
print("The subtotal is:",noIVA)
total=noIVA*0.16
total2=noIVA+total
print("The total is:",total2)
#End
#float con decimal e int sin decimales

