from ListaAzulejos import *

class Patrones():
    def __init__(self, codigo, cadena):
        self.codigo = codigo
        self.cadena = cadena
        self.casillas = ListaAzulejos() #Matriz
        self.siguiente = None
        self.anterior = None

    def agregarCasillas(self, casillas):
        self.casillas.insertar(casillas)

class ListaPatrones(object):
    def __init__(self):
        self.cabeza =  None
        self.cola = None
        self.contador = 0


    def insertar(self,  codigo, cadena, casillas):
        nodo = Patrones( codigo, cadena)
        nodo.casillas = casillas

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
            print(actual.codigo)
            actual = actual.siguiente
            
    def Seleccionar(self):
        actual = self.cabeza
        i=1
        Seleccionar = ""
        print("======Menu Nuevo Patron======")
        while actual:
            print(" ",actual.codigo)
            i+=1
            actual = actual.siguiente
        print(" exit. Regresar al menu principal")
        SeleccionarPiso = input("Ingrese el nombre del piso a graficar: ")
        actual = self.cabeza
        for piso in range(i):
            if SeleccionarPiso == actual.nombre:
                ListaAzulejos.graficar
            elif SeleccionarPiso == "exit":
               print("Help")
               #MenuInicial.MenuInicial()
            else:
                "Ingrese una entrada válida"
            piso +=1
    