
#funcion suma
def suma(a, b):
    
    resultado = a + b
    return resultado
    
#funcion par
def es_par(num):
   bandera = False
   if num % 2==0:
       bandera = True
   return bandera
   
#funcion conversion temperatura ºF = (ºC · 1,8) + 32
def celsius_a_fahrenheit(gradosC):
    gradosf = (gradosC * 1.8) + 32
    return gradosf

#funcion mayor de 3
def max_de_tres(num1, num2, num3):
    
    
    
#funcion validar nombre
def validar_nombre (nombre1):
    while nombre1 == "":
        return "nombre vacio ingreselo denuevo"
    