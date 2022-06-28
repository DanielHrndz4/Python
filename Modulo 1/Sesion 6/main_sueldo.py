#from calculos.isr import saludos

#saludos()

#from Calculos import isr
#isr.saludo()

#from Calculos.isr import *
#saludo()

#import sys 
#sys.path.append(r'C:\Users\MINEDUCYT\Desktop\Python\Modulo 1\Sesion 6')

#from Calculos.isr import saludo
#saludo()

from Calculos import isr

opc = "si"

def main():
    while opc != "no":
        print("""
        **********************************************
                    Elija una opcion
        [1] ISSS
        [2] AFP
        [3] ISR
        [4] Descuentos
        [5] Sueldo Gravable
        [6] Sueldo a Pagar 
        [7] Salir 
        **********************************************
        """)
        op = int(input("Digite la opcion: "))
        if op>=1 and op<=7:
            if op==1:
                sueldo = float(input("Digite su sueldo: "))
                ISSS = isr.isss(sueldo)
                print(f"El ISSS es: ${ISSS:.2f}")
            elif op==2:
                sueldo = float(input("Digite su sueldo: "))
                AFP = isr.afp(sueldo)
                print(f"El AFP es: ${AFP:.2f}")
            elif op==3:
                sueldo = float(input("Digite su sueldo: "))
                ISR = isr.isr(sueldo)
                print(f"El ISR es: ${ISR:.2f}")
            elif op==4:
                sueldo = float(input("Digite su sueldo: "))
                DES = isr.descuento(sueldo)
                print(f"El descuento es: ${DES:.2f}")
            elif op==5:
                sueldo = float(input("Digite su sueldo: "))
                SG = isr.sueldoGravable(sueldo)
                print(f"El sueldo gravable: ${SG:.2f}")
            elif op==6:
                sueldo = float(input("Digite su sueldo: "))
                SP = isr.sueldoPagar(sueldo)
                print(f"El sueldo a pagar es: ${SP:.2f}")
            elif op==7:
                print("Esta saliendo del programa...")
                exit()
                
if __name__=="__main__":
    main()
