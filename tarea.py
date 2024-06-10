class Tarea:
    def __init__(self, id, tarea, descripcion, estado):
        self.id = id
        self.tarea = tarea
        self.descripcion = descripcion
        self.estado = estado
    def __str__(self):
        return  f"ID: {self.id}\nTarea: {self.tarea}\nDescripcion: {self.descripcion}\nEstado: {self.estado}"
    def getTarea(self):
        return self.tarea
    
    def setTarea(self, tarea):
        self.tarea = tarea

    def getDescripcion(self):
        return self.descripcion
    
    def setDescripcion(self, descripcion):
        self.descripcion = descripcion
    
    def getEstado(self):
        return self.estado

    def setEstado(self, estado):
        self.estado = estado

   