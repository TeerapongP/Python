class Customer:
    name_ = ""
    last_name_ = ""
    _age_ = 0
    
    def add_cart(self):
        print("Add to cart ",self.name_,self.last_name_,self._age_)

Customer_1 = Customer()   
Customer_1.name_ = "Teerapong"
Customer_1.last_name_ = "Pinkaew"
Customer_1._age_ = "20"
Customer_1.add_cart()