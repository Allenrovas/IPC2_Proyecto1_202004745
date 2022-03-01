from ListaPatrones import ListaPatrones

class Piso():
    def __init__(self, nombre, rows, columns, flip, slide, siguiente= None, anterior = None):
        self.nombre = nombre
        self.filas = rows
        self.columnas = columns
        self.flip_costo = flip
        self.slide_costo = slide
        self.siguiente = None
        self.patrones = ListaPatrones()
        self.casillas = Matriz() #Matriz
        self.siguiente = siguiente
        self.anterior = anterior

    def agregarPatrones(self, patrones):
        self.patrones.insertar(patrones)

    def agregarCasillas(self, casillas):
        self.casillas.insertar(casillas)

class Patrones():
    def __init__(self, codigo, rows, columns, color, siguiente= None, anterior = None):
        self.codigo = codigo
        self.filas = rows
        self.columns = columns
        self.color = color
        self.siguiente = siguiente
        self.anterior = anterior
