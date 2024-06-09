from tarea import Tarea
from listraSimple import ListaSimple

lista = ListaSimple()
idTarea = 0 

# TODO: menu prioncipal
def menuPrincipal():
    opcion = 0
    while  True:
        print("========MI ADMIN DE TAREAS========")
        imprirTareas()
        print("= 1. Agregar Tarea               =")
        print("= 2. Marcar tarea 'En progreso'  =")
        print("= 3. Marcar tarea como terminado =")
        print("= 4. Ver lista de tareas         =")
        print("= 5. Ver informacion             =")
        print("= 6. Salir                       =")
        opcion = input("Elige una opcion: ")
        try:
            opcion = int(opcion)
            match opcion:
                case 1:
                    agregarTareas()
                case 2: 
                    cambiarEstado()
                case 3: 
                    eliminarTareas()
                case 4:
                    pass
                case 5:
                    print("============Informacion============")
                    print("=Nombre: Alexander Samuel Us Upun =")
                    print("=Carnet:  202300824               =")
                    print("=Curso: IPC2                      =")
                    
                case 6: 
                    print("Saliendo del programa...")
                    break
                case _: 
                    print("[Error]-Opcion invalida") 
        except:
            print("Opcion no valida, unicamente se aceptan enteros")
# TODO: imprimir las tareas:
def imprirTareas():
    if lista.tamaño == 0:
        print("==================================") 
        print("No hay tareas asignadas")
        print("==================================") 
    else:
        print("==================================") 
        lista.imprimirLista() 
        print("==================================")  

# TODO: Agregar Tareas
def agregarTareas():
    global lista
    global idTarea
   #print("==================================") 
    print("=========AGREGAR TAREA ===========") 
    id = idTarea
    tarea = input("Nombre de la tarea: ")
    descripcion = input("Agrega una descripcion de la tarea: ")
    estado = "pendiente"
    dato = Tarea(id, tarea, descripcion, estado)
    idTarea +=1
    lista.insertar(dato)
    
def cambiarEstado():
    global lista
    global idTarea
    print("=========TAREA EN PROGRESO========") 
    id = input("Ingresar el ID de la tarea: ")
    lista.obtenerUsuario(id) 



if __name__ == "__main__":
    menuPrincipal()