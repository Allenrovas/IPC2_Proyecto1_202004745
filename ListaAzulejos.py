class Azulejo():
    def __init__(self, rows, columns, color,cantidadrows,cantidadcolumns):
        self.cantidadrows = cantidadrows
        self.cantidadcolumns = cantidadcolumns
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


    def insertar(self, rows, columns, color,cantidadrows,cantidadcolumns):
        nodo = Azulejo(rows, columns, color,cantidadrows,cantidadcolumns)
        if self.cabeza is None:
            self.cabeza = nodo
            self.cola = self.cabeza
        else:
            nodo.anterior = self.cola
            self.cola.siguiente = nodo
            self.cola = nodo
        
        self.contador += 1

    
    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.color," ",actual.columns," ",actual.rows)
            actual = actual.siguiente

    def graficar(self):
        actual = self.cabeza
        nodo = 0
        archivo = open("GraphvizRep.dot", "w")
        archivo.write('digraph grid {bgcolor="slategrey" label="Reporte Graphviz"')
        archivo.write('layout=dot \n labelloc = "t"')
        archivo.write('edge [weigth=1000 style=dashed color=red4 dir = "both" arrowtail="open" arrowhead="open"]\n')
        archivo.write('rankdir="LR"\n')
        archivo.write("node[shape=box, color=lightgrey]") 
        archivo.write("a0 [label=<\n"+"<TABLE><TR>")
        ContadorC = 0
        while actual!= None:
            if ContadorC < actual.cantidadcolumns:
                if actual.color == "W":
                    archivo.write('<TD bgcolor="white"></TD>\n')
                elif actual.color == "B":
                    archivo.write('<TD bgcolor="black"></TD>\n')
                ContadorC += 1
                actual = actual.siguiente
            else:
                ContadorC = 0
                archivo.write("</TR><TR>")

        archivo.write("</TR></TABLE>>]")
        archivo.write("}")
        archivo.close()
        from os import system
        from os import system, startfile
        system('dot.exe -Tpng GraphvizRep.dot -o GraphvizRep.png')
        system('GraphvizRep.png')
            
            