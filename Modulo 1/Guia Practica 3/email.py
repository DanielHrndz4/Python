inicio = True
while(inicio==True):
    def validacion(a):
        if "@" in email:
            print ("Es valido...")
        else:
            print("No es valido...")

    email = input('Digite su correo electronico: ')
    validacion(email)
    input()
