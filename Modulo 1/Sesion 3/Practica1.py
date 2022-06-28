inicio = 1

while(inicio == 1):
     año = int(input("Digite el año: "))
     if año % 4 == 0 and (not(año%100==0) or año%400==0):
          print (año ,"Es biciesto")
     else:
          print (año, "No es bisiesto")
     print(" ")
   