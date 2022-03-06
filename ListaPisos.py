from pip import main
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
        
        self.siguiente = None
        self.anterior = None

    def agregarPatrones(self, patrones):
        self.patrones.insertar(patrones)

    

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
    
    def recorrermenu(self):
        actual =self.cabeza
        i=1
        SeleccionarPiso = ""
        print("======Menu Pisos======")
        while actual:
            print(" ",actual.nombre)
            i+=1
            actual = actual.siguiente
        print(" exit. Regresar al menu principal")
        SeleccionarPiso = input("Ingrese el nombre del piso a graficar: ")
        actual = self.cabeza

        while actual:
            if SeleccionarPiso == actual.nombre:
                actual.patrones.cabeza.casillas.graficar()
            elif SeleccionarPiso == "exit":
               print("Help")
               main.MenuInicial()
            else:
                "Ingrese una entrada válida"
            actual = actual.siguiente
            

        

        



    def ordenar_alfabeticamente(self):
        if self.contador > 1:
                while True:
                    actual = self.cabeza
                    i = None  # anterior
                    j = self.cabeza.siguiente  # siguiente
                    cambio = False
                    while j != None:
                        
                        if actual.nombre > j.nombre:
                            cambio = True
                            if i != None:
                                tmp = j.siguiente
                                i.siguiente = j
                                j.siguiente = actual
                                actual.siguiente = tmp
                            else:
                                tmp2 = j.siguiente
                                self.cabeza = j
                                j.siguiente = actual
                                actual.siguiente = tmp2
                            i = j
                            j = actual.siguiente
                        else:
                            i = actual
                            actual = j
                            j = j.siguiente
                    if not cambio:
                        break  
            