class Usuario:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.tareas = []

    def agregarTarea(self, tarea):
        self.tareas.append(tarea)

<<<<<<< HEAD
    def listarTareas(self):
   for tarea in self.tareas:
       if tarea.estaLista():
           print(f"La tarea {tarea.obtenerNombre()} está lista")
       else: <<<<<<< Elimina esta
           print(f"La tarea {tarea.obtenerNombre()} no está lista")
=======
>>>>>>> f77f663607f7ba04d29a0ad7cd1bd77cbe64a1e5
