class Products:
    def __init__(self, name, price, category):
        self.name=name
        self.price=price
        self.category=category
        
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += self.price*percent_change
        else:
            self.price -= self.price*percent_change
            
    def print_info(self):
        print(f'Name of product: {self.name} \nCategory: {self.category} \nPrice {self.price}')
        
a=Products('Apple', 23 , 2)
a.print_info()
 
 
class Store:
    def __init__(self, name):
        self.name=name
        self.my_products=[]
        self.product=Products(name = 'Zuma', price =1, category='clothes')
        
        
    def add_product(self, new_product):
        self.my_products.append(new_product)
        
    def sell_product(self, id):
        self.my_products.remove(self.my_products[id])
        print(f'Name of product: {self.product.name} \nPrice: {self.product.price} \nCategory: {self.product.category}')
        
    def inflation(self, percent_increase):
        return Products.update_price(self, percent_increase, True)
    
    def set_clearance(self, category, percent_discount):
        return Products.update_price(self, percent_discount, False)

