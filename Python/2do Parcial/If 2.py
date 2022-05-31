while True:
    x=5
    y=int(input("Guess the number:"))
    if y<x:
      print('You need more')
    if y>x:
      print('You need less')
    if x==y:
      print('Congatulations')