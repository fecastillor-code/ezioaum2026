#FUNCION SIN ARGUMENTO SIN RETORNO
def funcion_bkn():
    print("FUNCION BKN Y SENCILLA")

funcion_bkn()

#CON RETORNO
def suma():
    num1=1
    num2=1
    return(num1+num2)

print("la suma de ambos numeros es: ",suma())


#FUNCION CON ARGUMENTO SIN RETORNO

def suma(a,b):
    sumar= a + b
    print(f"la suma de ambos numeros es {sumar}")
num1=int(input("INGRESE EL PRIMER NUMERO: "))
num2=int(input("INGRESE EL SEGUNDO NUMERO: "))
suma(num1,num2)

# CON RETORNO

def suma(a,b):
    sumar= a +b
    return(sumar)
num1=int(input("INGRESE EL PRIMER NUMERO: "))
num2=int(input("INGRESE EL SEGUNDO NUMERO: "))

print(f"LA SUMA DE AMBOS NUMEROS ES {num1 + num2}")