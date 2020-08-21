import Products
class Store:
    def __init__(self, name):
        self.name=name
        self.my_products=[]
        self.product=Products(name, price, category)
        
        
    def add_product(self, new_product):
        self.my_products.append(new_product)
        
    def sell_product(self, id):
        self.my_products.remove(self.my_products[id])
        print(f'Name of product: {self.name} \nPrice: {self.price} \nCategory: {product_info.category}')

    # def inflation(self, percent_increase):
            # self.price += self.price*percent_change
        
            # self.price -= self.price*percent_change
            

    