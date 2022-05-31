import datetime

dia= datetime.date.today()
w= dia.weekday()+1

if(w==0):
  print("feliz domingo")
elif(w==1):
  print("Buen inicio de semana, ¡hoy es lunes!")
elif(w==2):
  print("Hoy es martes")
elif(w==3):
  print("Hoy es miércoles")
elif(w==4):
  print("Hoy es jueves")
elif(w==5):
  print("Se acabaron las clases,¡hoy es viernes!")
elif(w==6):
  print("Hora de descansar, ¡hoy es sabado! ")