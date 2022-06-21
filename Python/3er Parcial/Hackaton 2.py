print("Welcome to the elevator")
yu=int(input("In what floor are you now 1(low level), 2(intermediate level) or 3(top floor):\n"))
while True:
  if yu==1:
    print("You are in floor 1")
    yu=int(input("Where do you want to go floor 2 or 3:\n"))
  if yu==2:
    print("You are in floor 2")
    yu=int(input("Where do you want to go floor 1 or 3:\n"))
  if yu==3:
    print("You are in floor 3")
    yu=int(input("Where do you want to go floor 1 or 2:\n"))
    