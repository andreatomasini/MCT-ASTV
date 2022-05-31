while True:
  speed=int(input("Write the speed:"))
  if speed>=25:
    print("Critical Alert!!!")
  elif speed>=20:
    print("Lightning in the sky!!!")
  elif speed>=10:
    print("Shooting Star!!")
  else:
    print("Nothing to see here")