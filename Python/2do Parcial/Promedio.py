print("Avarage")
while True:
  g1=float(input("Write the first number:"))
  g2=float(input("Write the second number:"))
  g3=float(input("Write the third number:"))
  pro=g1+g2+g3
  pro1=pro/3
  print("Your avarage is",pro1)
  if(pro1>=9):
    print('You won a reward, congratulations!!!!')
  
  if(pro1<9):
    print('You need to make more effort ')
  if(pro1<6):
    print('You failed')