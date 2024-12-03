import time

class InventoryService:
    def __init__(self, mediator):
        self.mediator = mediator
        self.mediator.subscribe("OrderPlaced", self.update_inventory)

    def update_inventory(self, data):
        """
        Actualiza el inventario cuando se recibe un evento de 'OrderPlaced'.
        """
        time.sleep(0.5)  # Simula el retraso de inventario
        print(f"InventoryService: Inventario actualizado para el pedido {data['order_id']}.")
        self.mediator.publish("InventoryUpdated", data)
