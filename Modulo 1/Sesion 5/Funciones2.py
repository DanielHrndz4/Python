#VALORES POR DEFAULT EN UNA FUNCION
def calculo_desc(sueldo:float, isss:float=0.03,afp:float=0.0725) -> float:
    #DOCUMENTACION
    """
    La funcion calculo_desc realiza el calculo de descuento de ISSS y AFP segun el sueldo
    Parametro ISSS es opcional y su valor por default es 3%
    Parametro AFP es opcional y su valor por default es 7.25%
    El retorno es la suma de ISSS y AFP
    """
    desc = sueldo * isss + sueldo * afp
    return desc
descuento = calculo_desc(800)
print(f"Los descuentos de isss y afp son: {descuento}")
#FORMAS DE IMPRIMIRLO
descuento2 = calculo_desc(800,0.04)
descuento3 = calculo_desc(800,0.04,0.06)
descuento4 = calculo_desc(800,afp=0.06)
descuento2 = calculo_desc(800,isss=0.04)
descuento2 = calculo_desc(800,afp=0.06,isss=0.04)

#ARGUMENTOS VARIABLES CON UNA LISTA (*=LISTA)
print('alicia','beto','carlos',12,True)
def listar_nombres(*nombres):
    for nombre in nombres:
        print(nombre)
listar_nombres('alicia','beto','carlos',12,True,'daniel','jonathan')

#ARGUMENTOS VARIABLES CLAVE:VALOR (**DICCIONARIOS)
def listar_diccionarios(**terminos):
    for k,v in terminos.items():
        print(k,v)
listar_diccionarios(
    PK='Primary Key',
    FK='Foreign Key',
    UQ='Unique')