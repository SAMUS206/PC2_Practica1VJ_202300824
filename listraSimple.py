import subprocess
from Nodo import Nodo
import os
class ListaSimple:
    def __init__(self):
        self.cabeza = None
        self.tamaño = 0

    def __len__(self):
        return self.tamaño
    
    # Todo: insertar al final de la lista
    

    def insertar(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza == None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente != None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self.tamaño += 1
        

    def imprimirLista(self):
        actual = self.cabeza
        while actual != None:
            print(actual.dato)
            actual = actual.siguiente 
        
    def buscarTarea(self, id):
        if self.cabeza is None:
            print("Lista vacía")
            return None
        actual = self.cabeza
        while actual != None:
            if actual.dato.id != id:
                pass
            else: 
                return actual.dato
            actual = actual.siguiente
        
    
    def cambiarEstado(self, id, estado):
        tarea = self.buscarTarea(id)
        if tarea and tarea.id == id:
            tarea.setEstado(estado)
            print(f"El estado de la tarea con ID {id} ha sido cambiado a '{estado}'.")
        else:
            if self.cabeza == None:
                pass
            else:   
                print(f"No se encontró la tarea con ID {id}.")

    def eliminar(self, id):
        if self.cabeza is None:
            print("Lista vacía")
            return None
        actual = self.cabeza
        anterior = None
        while actual != None:
            if actual.dato.id != id:
                print("ID no encontrado")
            else:
                if anterior == None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                self.tamaño -= 1
                break
            anterior = actual
            actual = actual.siguiente
    
    def graficar(self):
        try:
            if self.cabeza is None:
                print("La lista está vacía. No se puede generar el gráfico.")
                return
            
            codigodot = '''digraph G {
rankdir=LR;
node [shape = record, height = .1]
'''

            actual = self.cabeza
            contador_nodos = 0
            
            while actual is not None:
                codigodot += 'node'+str(contador_nodos)+' [label = "{'+ str(actual.dato).replace("\n", "\\n") +'}"];\n'
                contador_nodos += 1
                actual = actual.siguiente

            actual = self.cabeza
            contador_nodos = 0
            while actual is not None and actual.siguiente is not None:
                codigodot += 'node'+str(contador_nodos)+' -> node'+str(contador_nodos+1)+';\n'
                contador_nodos += 1
                actual = actual.siguiente

            codigodot += '}'
            
            with open('reportedot/lista.dot', 'w') as archivo:
                archivo.write(codigodot)

            # Generar la imagen
            ruta_dot = 'reportedot/lista.dot'
            ruta_reporte = 'reportes/lista_simple.png'
            comando = f'dot -Tpng {ruta_dot} -o {ruta_reporte}'
            resultado = os.system(comando)
            if resultado != 0:
                print("Error al generar la imagen con Graphviz. Asegúrate de que Graphviz esté instalado y accesible desde la línea de comandos.")
                return

            # Abrir la imagen
            ruta_abrir_reporte = os.path.abspath(ruta_reporte)
            if os.name == 'posix':
                subprocess.run(['xdg-open', ruta_abrir_reporte])
            else:
                os.startfile(ruta_abrir_reporte)
            print('Reporte generado con éxito')
        except Exception as e:
            print(f"Se produjo una excepción: {e}")