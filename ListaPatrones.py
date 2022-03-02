class Patrones():
    def __init__(self, codigo, cadena):
        self.codigo = codigo
        self.cadena = cadena
        self.siguiente = None
        self.anterior = None

class ListaPatrones(object):
    def __init__(self):
        self.cabeza =  None
        self.cola = None
        self.contador = 0


    def insertar(self,  codigo, cadena):
        nodo = Patrones( codigo, cadena)

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
            print(" "+actual.codigo)
            actual = actual.siguiente
            