while True:
  suma=int(input("Write a number:"))
  n=int(input("Write the number of repetitions of the number:"))
  s=int(input("Write how much is added to the first number:"))
  for x in range(n):
      suma=suma+s
      print(suma)

      
  x=input("Do you want to continue?")
  if(x=="yes"):
    continue
  else:
     break
    
