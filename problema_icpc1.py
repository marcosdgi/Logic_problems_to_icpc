longitud = int(input("ingrese la longitud de su lista:"))
class consultas():
    lista = [0 for _ in range(longitud)]
    i = 1
    j = 1
    v = 1

    def __init__(self, i, j, v):
        self.i = i
        self.j = j
        self.v = v
        
    def consulta_1(self):
        
        if self.i <= longitud and self.j < longitud and self.v <= 1000 and self.v >= 1:
            
            for i in range(self.i, self.j-1):
                self.lista[i] = self.v
                
            return self.lista
        else:
            return "El valor de las variables introducidas es mayor que el tamaño de la lista"
    def consulta_2(self):
        if self.i and self.j >= 1 <= longitud:

            for i in range(self.i,self.j-1):
                for j in range(self.i,self.j-1):
                    
                    self.lista[i] = j - i + 1

            return self.lista
        else:
            return "El valor de las variables introducidas es mayor que el tamaño de la lista"
        
    def consulta_3(self,lista):
        cont = 0
        if self.i and self.j >= 1 <= longitud:
            for i in lista:
                if lista[i] != 0 and lista[i] % 5 == 0:
                    cont += 1
                    return cont
                else: 
                    continue
        else:
            return "El valor de las variables introducidas es mayor que el tamaño de la lista"
                        
primera_consulta = consultas(2,11,4)
res = primera_consulta.consulta_2()
res2 = primera_consulta.consulta_3(res)

print(res2)
print(res)

