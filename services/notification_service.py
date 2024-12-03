class NotificationService:
    def __init__(self, mediator):
        self.mediator = mediator
        self.mediator.subscribe("PaymentSuccessful", self.notify_user)

    def notify_user(self, data):
        """
        Envía una notificación al usuario.
        """
        print(f"NotificationService: Notificación enviada para el pedido {data['order_id']}.")
