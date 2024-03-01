from locust import HttpUser, task, between
from random import randint
from json.decoder import JSONDecodeError

class WebsiteUser(HttpUser):
    wait_time= between(1,5)
    cart_id= None

    @task(2)
    def view_products(self):
        print('view products')
        collection_id = randint(2,6)
        self.client.get(
            f'/store/products/?collection_id={collection_id}',
            name= '/store/products'
        )
    @task(4)
    def view_product(self):
        print('view product details')
        product_id= randint(1, 1000)
        self.client.get(
            f'/store/produts/{product_id}',
            name= '/store/products/:id'
        )  
    @task(1)
    def add_to_cart(self):
        print('add to cart')
        if self.cart_id is None:
            print("Cart ID is not initialized. Make sure to call on_start first.")
            return
        product_id= (1, 10)
        self.client.post(
            f'/store/carts/{self.cart_id}/items/',
            name= '/store/carts/items',
            json={'product_id':product_id, 'quantity': 1}
        )
    def on_start(self):
        try:
            response = self.client.post(f'/store/carts')
            result = response.json()
            self.cart_id = result['id']
        except JSONDecodeError as e:
            print(f"Error decoding JSON response: {e}")
            print(f"Response content: {response.content}") 
    @task(1)
    def say_hello(self):
        self.client.get('/playground/hello/')


