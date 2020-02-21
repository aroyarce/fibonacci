import json
import math

#Usar mayor a 0.
def Fibonacci_Recursivo(numero):
    if (numero == 1):
        return 0
    if (numero == 2):
        return 1
    if (numero == 3):
        return 1
    
    aux = Fibonacci_Recursivo(numero-1)+Fibonacci_Recursivo(numero-2)
    return aux
        
#Funciona bien hasta n=100
def Fibonacci_loop(numero):
    aux1=0
    aux2=1

    if (numero == 1):
        return 0
    if (numero == 2):
        return 1
    if (numero == 3):
        return 1
        
    for i in range(numero):
        aux3=aux1
        aux1=aux2
        aux2=aux3+aux2
    
    return aux2
        
def lambda_handler(event, context):
    # TODO implement
    statusCode = 200
    resultadoStr = 'Hello from Lambda!'
    print("***************************************")
    print("Eventos valors y parametros")
    
    numeroaux = event["numero"]
    try:
        # TODO: write code...
        numeroaux = int(numeroaux)
        print("Convertido a Int")
    except e:
        print("Excepcion, no se puede comvertir a int")
        statusCode = 300
        resultadoStr = 'No es un numero'
        return {
            'statusCode': statusCode,
            'body': json.dumps(resultadoStr)
        }
        
    if (isinstance(numeroaux, int)):
        if(numeroaux == 0):
            statusCode = 400
            resultadoStr = 'Es un Cero.'
        elif(numeroaux >= 101):
            statusCode = 401
            resultadoStr = 'Es mayor a 100'
        else:
            #salida1 = Fibonacci_Recursivo(numeroaux);
            salida1 = Fibonacci_loop(numeroaux);
            statusCode = 200
            resultadoStr = salida1
            print(salida1)
                
    return {
        'statusCode': statusCode,
        'body': resultadoStr,
        'salida': str(salida1)
    }
