
palabra = 'pinga'

abecedario = [
    'a','b','c','d','e','f','g','h','i','j','k',
    'l','m','n','o','p','q','r','s','t','u','v','w','y','z'
]
valores = [
    2,3,4,5,6,7,8,9,10,11,
    12,14,15,16,17,18,19,20,21,22,23,24,25
]
suma = 0
def suma_comprobatoria(palabra_determinada):
    suma = 0
    for letra in palabra:
        for char in abecedario:
            if char.__eq__(letra):
                posicion = palabra.index(char)
                posicion_list = abecedario.index(char)
        suma+= valores[posicion_list]*posicion
    print(suma,palabra)
suma_comprobatoria(palabra)