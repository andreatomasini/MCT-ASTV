#Homework areas
print("Triangle area")
BASE=int(input("Write the base of the triangle:"))
ALTURA=int(input("Write the height of the triangle:"))
Multiplicación=BASE*ALTURA
print("The area of the triangle is:",Multiplicación/2)
print("Rectangle area")
BASE=int(input("Write the base of the rectangle:"))
ALTURA=int(input("Write the height of the rectangle:"))
print("The area of the rectangle is:",BASE*ALTURA)
print("Pentagon area")
LADO=int(input("Write the side of the pentagon:"))
PERIMETRO= LADO*5
APOTEMA=int(input("Write the apotema:"))
ApPe=PERIMETRO*APOTEMA
print("The area of the pentagon is:",ApPe/2)
print("Circle area/pi is 3.14")
RADIO=int(input("Write the radio of the circle:"))
radio2= RADIO*RADIO
print("The area of the circle is:",radio2*3.14)
print("Symmetrical trapezoid area")
D1=int(input("Write the diagonal 1:"))
D2=int(input("Write the diagonal 2:"))
D=D1*D2
print("The trapezoid area is:",D/2)
print("Asymmetric trapezoid area")
T1=int(input("Write trangle 1 base:"))
TR1=int(input("Write triangle 1 heght:"))
TRI=T1*TR1
T=TRI/2
T2=int(input("Write trangle 2 base:"))
TR2=int(input("Write triangle 2 heght:"))
TRI2=T2*TR2
t2=TRI2/2
print("The trapezoid area is:",t2+T)
print("Rhombus area")
DM=int(input("Write the major diagonal:"))
Dm=int(input("Write the minor diagonal:"))
D=DM*Dm
print("The area of the rhombus is:",D/2)
print("END")