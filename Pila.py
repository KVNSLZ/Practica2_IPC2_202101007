from Nodo import Nodo
import graphviz

class Pila:
    def __init__(self):
        self.tope = None
        self.valor = None

    def insertar(self, valor):

        if self.tope == None:
            self.tope = Nodo(valor)
        else:
            nodoTemp = Nodo(valor)
            nodoTemp.setSiguiente(self.tope)
            self.tope = nodoTemp

    def printPila(self):
        nodoTemp = self.tope
        listaDatos = ""
        while nodoTemp != None:
            listaDatos += nodoTemp.getValor()
            nodoTemp = nodoTemp.getSiguiente()
        return listaDatos
    
    def generarDot(self):
        nodoTemp = self.tope
        dot = graphviz.Digraph('structs', filename='structs.gv', node_attr={'shape': 'none', 'fontname':'Helvetica'})
        
        strTabla = "<table>"

        while(nodoTemp != None):
            strTabla += f'<tr><td width="60" height="60" border="0">{nodoTemp.getValor()}</td></tr>'
            nodoTemp = nodoTemp.getSiguiente()
        
        strTabla += "</table>"

        dot.node('n', label='<' +strTabla+'>')
        dot.render(outfile='img/structs.png').replace('\\', '/')
        'img/structs.png'

        return "imagen creada con exito"