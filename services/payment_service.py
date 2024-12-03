import time

class PaymentService:
    def __init__(self, mediator):
        self.mediator = mediator
        self.mediator.subscribe("OrderPlaced", self.process_payment)

    def process_payment(self, data):
        """
        Procesa el pago cuando se recibe un evento de 'OrderPlaced'.
        """
        time.sleep(1)  # Simula el procesamiento del pago
        print(f"PaymentService: Pago procesado para el pedido {data['order_id']}.")
        self.mediator.publish("PaymentSuccessful", data)
