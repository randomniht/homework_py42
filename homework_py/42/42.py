import json
class Model:
    def __init__(self,controller):
        self.controller = controller
    def puck_json(self,total_product):
        self.controller.add()
        with open('menu.json','w', encoding='utf-8') as f:
           f = total_product
           json.dump(f) 
    
class View:
    pass
class Controller:
    def  __init__(self,model):
        self.model = model
        pass
    def add(self,product,price):
        total_product = {product:price}
model = Model
controller = Controller



