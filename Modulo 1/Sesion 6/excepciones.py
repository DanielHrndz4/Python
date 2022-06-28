from typing import Type
def main():
    # try:
    #     nput("Digite la palabra: ")
    # except:
    #     print("\nAdios...")
    
    # try:
    #     4/0
    # except Exception as e:
    #     print("\nError", e)

    input("Digite la palabra: ")
if __name__ == "__main__":
    try:
        #4/0
        "Hola"+4
        main()
    except KeyboardInterrupt as e:
        print("Saliendo...")
    except ZeroDivisionError as e:
        print("Division entre cero no permitida...")
    except TypeError as e:
        print("Operacion no permitida...")
    else:
        print("No hubo errores")
    finally:
        print("Error o no aqui estoy")

    suma = 6+4
    print(f"La suma es: {suma}")
