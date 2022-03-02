from ListaAzulejos import ListaAzulejos
from ListaPatrones import ListaPatrones

class Piso():
    def __init__(self, nombre, rows, columns, flip, slide):
        self.nombre = nombre
        self.rows = rows
        self.columns = columns
        self.flip = flip
        self.slide = slide
        self.patrones = ListaPatrones()
        self.casillas = ListaAzulejos() #Matriz
        self.siguiente = None
        self.anterior = None

    def agregarPatrones(self, patrones):
        self.patrones.insertar(patrones)

    def agregarCasillas(self, casillas):
        self.casillas.insertar(casillas)

class ListaPisos(object):
    def __init__(self):
        self.cabeza =  None
        self.cola = None
        self.contador = 0


    def insertar(self,  nodo):
        nodo = nodo

        if self.cabeza is None:
            self.cabeza = nodo
            self.cola = self.cabeza
        else:
            nodo.anterior = self.cola
            self.cola.siguiente = nodo
            self.cola = nodo
        
        self.contador += 1

    
    def recorrer(self):
        actual = self.cabeza
        
        while actual:
            print(actual.nombre)
            actual.patrones.recorrer()
            actual = actual.siguiente
            