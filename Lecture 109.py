class Animal:
    def eat(self):
        print("Eating Eating!")

class Cat(Animal):
    cat_name = ""

    def set_name(self,text):
        self.cat_name = text
        print("Setting new Cat Name ",self.cat_name)
    def eat(self):
        print("Meoww !!",self.cat_name)


cat1 = Cat()
cat1.set_name("Auri")
cat1.eat()
