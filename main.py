import imp
from Nodos import *
from ListaAzulejos import *
from ListaPatrones import *
from ListaPisos import *
from tkinter import *
import xml.etree.ElementTree as ET
from tkinter.filedialog import askopenfilename
listapisos = ListaPisos()

def LeerXml():
    Contador = 0
    columns = ""
    rows = ""
    flip = ""
    slide = ""
    archivoinput = askopenfilename(filetypes=[("Archivos XML", ".xml"), ("All Files", ".*")])
    xmlentrada = ET.parse(archivoinput)
    raizxml = xmlentrada.getroot()
    for hijo in raizxml:
        nombre = hijo.attrib['nombre']
        Contador=0
        for subhijo in hijo:
            if Contador == 0:
                rows = subhijo.text
                rows = int(rows)
            if Contador == 1:
                columns = int(subhijo.text)
            if Contador == 2:
                flip = int(subhijo.text)
            if Contador == 3:
                slide = int(subhijo.text)
            if Contador == 4:
                nodo = Piso(nombre, rows,columns, flip, slide)
                for subhijo2 in subhijo:
                    codigo = subhijo2.attrib['codigo']
                    cadena = subhijo2.text
                    ContadorRows = 0
                    ContadorColumns = 0
                    for letra in cadena:
                        if ContadorColumns < columns:
                            nodo.casillas.insertar(ContadorRows,ContadorColumns,letra)
                            ContadorColumns+=1
                        else:
                            ContadorRows+=1
                            ContadorColumns=0
                    nodo.patrones.insertar(codigo, cadena)
                listapisos.insertar(nodo)
            Contador+=1

          

def MenuInicial():
    SeleccionarUsuario = 0
    print("         Menu Ventas")
    print("==============================================")
    print("Pulse el numero correspondiente a la solicitud")
    print("")
    print("1. Leer Archivo.")
    print("2. Ver un piso en específico")
    print("3. Ver todos los Pisos")
    print("4. Salir")
    print("")
    SeleccionarUsuario = int(input())
    if SeleccionarUsuario == 1:
        print("")
        LeerXml()
        MenuInicial()
    elif SeleccionarUsuario == 2:
        print("")
    elif SeleccionarUsuario == 3:
        listapisos.recorrer()
    elif SeleccionarUsuario ==4:
        print("Gracias por usar nuestro sistema, buen dia.")
        exit
    else:
        print("")
        print("Ingrese una entrada valida")
        print("")
        MenuInicial()

MenuInicial()

