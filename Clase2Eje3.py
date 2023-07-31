class Player:
    def __init__(self, name, color):
        # Atributos del jugador
        self.name = name
        self.color = color
        self.position = (0, 0) 
        self.is_alive = True
        self.is_impostor = False
        self.tasks = []
        self.sabotage_in_progress = False
        self.vent_cool_down = 0

    def move_to(self, x, y):    # Método para mover al jugador a la posición especificada en las coordenadas (x, y)
        self.position = (x, y)

    def kill_player(self, target_player):   # Método para permitir que un jugador impostor elimine a otro jugador si están en la misma ubicación
        if self.is_impostor and self.position == target_player.position:
            target_player.is_alive = False

    def complete_task(self, task):  # Método para permitir que un jugador tripulante complete una tarea específica de su lista de tareas
        if not self.is_impostor and task in self.tasks:
            self.tasks.remove(task)

    def report_dead_body(self, dead_player):  # Método para permitir que un jugador encuentre y reporte el cuerpo de un jugador muerto
        if not self.is_impostor and not dead_player.is_alive and self.position == dead_player.position:
            # Lógica para reportar un cuerpo muerto y manejar la reunión de emergencia.
            pass

    def use_vent(self):  # Método para permitir que un jugador impostor use una ventilación para moverse rápidamente por el mapa
        if self.is_impostor and self.vent_cool_down == 0:
            # Lógica para usar una ventilación y moverse rápidamente por el mapa.
            self.vent_cool_down = 3  # Por ejemplo, establecer un tiempo de enfriamiento de 3 segundos.

    def sabotage_system(self, system):  # Método para permitir que un jugador impostor inicie un sabotaje en un sistema específico del juego
        if self.is_impostor:    # Lógica para iniciar un sabotaje en un sistema específico del juego.
            
            self.sabotage_in_progress = True
            # ... más lógica de manejo del sabotaje 