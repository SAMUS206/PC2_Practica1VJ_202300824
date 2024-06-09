from Nodo import Nodo

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
    
    def obtenerUsuario(self, id):
        actual = self.cabeza
        while actual != None:
            if actual.dato.id == id:
                return actual.dato
            actual = actual.siguiente
        return None
    
    def eliminar(self, id):
        actual = self.cabeza
        anterior = None
        while actual != None:
            if actual.dato.id == id:
                if anterior == None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                self.tamanio -= 1
                break
            anterior = actual
            actual = actual.siguiente
