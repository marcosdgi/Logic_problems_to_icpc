""" numero = int(input("ingrese el numero de casos de prueba:"))
 """
positivos = ['abc','acb','bac','cba']
negativos = ['bca','cab']

casos = positivos + negativos 

lista_de_respuestas = []

def analisis(numero,casos,positivos,negativos):
    if numero <=6 and numero >=1:
    
        for caso in casos:
            if caso in positivos:
            
                lista_de_respuestas.append("si")
        
            if caso in negativos:
                
                lista_de_respuestas.append("no")
                
        return lista_de_respuestas
                    

    else:
        return "Ingrese un numero menor que 6"
    

print(analisis(6,casos,positivos,negativos))




