from mediator import Mediator
from services.order_service import OrderService
from services.payment_service import PaymentService
from services.inventory_service import InventoryService
from services.notification_service import NotificationService

def main():
    # Crear Mediator
    mediator = Mediator()

    # Inicializar los servicios con el Mediator
    order_service = OrderService(mediator)
    payment_service = PaymentService(mediator)
    inventory_service = InventoryService(mediator)
    notification_service = NotificationService(mediator)

    # Crear un pedido (simulación de evento)
    order_service.create_order(101)

if __name__ == "__main__":
    main()
