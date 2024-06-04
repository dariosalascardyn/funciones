import os, time
os.system("cls")

#funcion sin argumento y sin retorno
def saludar():
    print("hola mundo en python soy una funcion indefensa")


#funcion con argumento y sin retorno
def sumar(num1, num2):
    resultado = num1 + num2 
    print(f"la suma de dos numeros es {resultado}")
    



#funcion sin argumento y con retorno
def despedir():
    return "chao"

    
#fucion con argumeno y con retorno
def sexoC_a_sexoS(genero):
    while genero != "f" and genero != "m":
        genero = input("ingrese sexo f o m\n")
    if genero == "m":
        return "masculino"
    else:
        return "femenino"
    

#funcion edad
def calcularEdad(a, b):

    resultado = a - b
    return resultado