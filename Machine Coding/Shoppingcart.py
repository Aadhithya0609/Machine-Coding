class ShoppingCart:
    def __init__(self,name,total):
        self.name=name
        self.total=total
    def addItem(self,price):
        self.total+=price
    def removeItem(self,price):
        self.total-=price
    def apply_coupon(self,percent):
        self.total-=self.total*percent/100
    def iseligibleforfree(self):
        if self.total >=1000:
            return True
        else:
            return False
    def display(self):
        return f"name:{self.name} \ntotal:{self.total}"
        
s1=ShoppingCart("Aadhi",0)
s1.addItem(10000)
s1.addItem(785)
s1.addItem(987)
s1.addItem(567)

s1.removeItem(678)
s1.apply_coupon(25)
print(s1.display())
print(s1.iseligibleforfree())

