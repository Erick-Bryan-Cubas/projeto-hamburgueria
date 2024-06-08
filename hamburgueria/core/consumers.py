import json
from channels.generic.websocket import WebsocketConsumer

class CartConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        data = json.loads(text_data)
        print('Received data:', data)  # Adicione esta linha para debug
        action = data.get('action')
        product_id = str(data.get('product_id', ''))
        quantity = int(data.get('quantity', 1))

        cart = self.scope['session'].get('cart', {})

        if action == 'add':
            if product_id in cart:
                cart[product_id] += quantity
            else:
                cart[product_id] = quantity
        elif action == 'remove':
            if product_id in cart:
                cart[product_id] -= quantity
                if cart[product_id] <= 0:
                    del cart[product_id]
        elif action == 'clear':
            cart = {}

        self.scope['session']['cart'] = cart
        self.scope['session'].save()

        print('Updated cart:', cart)  # Adicione esta linha para debug

        self.send(text_data=json.dumps({
            'status': 'success',
            'cart': cart
        }))
