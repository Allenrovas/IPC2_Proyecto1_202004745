
class Azulejo():
    def __init__(self, rows, columns, color):
        self.rows = rows 
        self.columns = columns
        self.color = color
        self.siguiente = None
        self.anterior = None
        
class ListaAzulejos(object):
    def __init__(self):
        self.cabeza =  None
        self.cola = None
        self.contador = 0


    def insertar(self, rows, columns, color):
        nodo = Azulejo(rows, columns, color)

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
            actual = actual.siguiente