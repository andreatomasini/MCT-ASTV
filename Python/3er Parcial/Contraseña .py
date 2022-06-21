
import random

base="abcdefghijknmñopqrstuvwxyz"




n=int(input("Write the numbers of the repetitions:"))

for i in range(n):
 passw=""
 e=int(input("Write the numbers of characters in the password:"))
 for i in range(e):
  passw=passw+random.choice(base)
 
 print("password", passw)
input()
 