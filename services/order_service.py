class OrderService:
    def __init__(self, mediator):
        self.mediator = mediator

    def create_order(self, order_id):
        """
        Emite un evento de creación de pedido.
        """
        print(f"OrderService: Pedido {order_id} creado.")
        self.mediator.publish("OrderPlaced", {"order_id": order_id})
