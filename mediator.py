class Mediator:
    def __init__(self):
        self.subscribers = {}  # Diccionario para manejar suscriptores por tipo de evento

    def subscribe(self, event_type, handler):
        """
        Registra un manejador para un evento específico.
        :param event_type: Tipo de evento.
        :param handler: Función que manejará el evento.
        """
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(handler)

    def publish(self, event_type, data):
        """
        Publica un evento y notifica a todos los manejadores suscritos.
        :param event_type: Tipo de evento.
        :param data: Información relacionada con el evento.
        """
        if event_type in self.subscribers:
            for handler in self.subscribers[event_type]:
                handler(data)
