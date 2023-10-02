import numpy as np

class Matriz ():
    matriz = np.random.choice([False],size=(0,0))
    complemento_matriz = np.random.choice([False],size=(0,0))
    lista_de_contadores = [int]
    vertices = 0
    def crear_matriz(self):
        self.matriz = np.random.choice([False],size=(self.vertices,self.vertices))   

   
    def armar_matriz(self,vert1, vert2):
        self.matriz[vert1-1][vert2-1] = True
        self.matriz[vert2-1][vert1-1] = True

    def hallar_complemento_matriz(self):
        self.complemento_matriz = np.random.choice([False],size=(self.vertices, self.vertices)) 
        for i in range(self.vertices):
            for j in range(self.vertices):
                if i != j:

                    if self.matriz[i][j]:
                        self.complemento_matriz[i][j] = False
                    else:
                        self.complemento_matriz[i][j] = True 

    def __init__(self, vertices) :
        self.vertices = vertices
        self.crear_matriz()

    def adyacente(self,fila):
        fila -= 1
        lista_adyacentes = [int]
        for i in range(self.vertices):
            if self.complemento_matriz[fila][i]:
                lista_adyacentes.append(i)
        return lista_adyacentes
    
    def camino(self,destino:int,inicio:int, visitados):
        cont = 0
        lista_de_adyacentes = [int]
            
        if destino != inicio:
            
            if inicio in visitados:
                return cont
            
            lista_de_adyacentes = self.adyacente(inicio)
        
            for i in range(1,len(lista_de_adyacentes)):
                visitados.append(lista_de_adyacentes[i])
                cont = self.camino(destino,lista_de_adyacentes[i], visitados)
                if len(visitados) == 0:        
                    self.lista_de_contadores.append(cont) 
                print(len(visitados))

        elif cont >= 1:
            cont += 1 

        else:
            cont += 1 
        
        
        
        return cont

def main ():
        ejemplo = Matriz(5)
        ejemplo.crear_matriz()
        ejemplo.armar_matriz(1,2)
        ejemplo.armar_matriz(2,3)
        ejemplo.armar_matriz(4,5)
        
        print(ejemplo.matriz)

        ejemplo.hallar_complemento_matriz()
        print(ejemplo.complemento_matriz)

        print(ejemplo.adyacente(2))
        
        ejemplo.camino(3,1,visitados=[])
        print(ejemplo.lista_de_contadores)
main()
