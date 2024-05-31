import json

def lambda_handler(event, context):
    #Extraccion de numeros del evento
    num1 = event['num1']
    num2 = event['num2']
    
    # Realizamos la operacion
    result = num1 * num2
    
    # Preparamos el response
    response = {
        'result': result
    }
    
    # Devolvemos el respone
    return{
        'statusCode': 200,
        'body': json.dumps(response)
    }