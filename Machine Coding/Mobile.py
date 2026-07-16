class Mobile:
    def __init__(self,brand,model,battery,storage):
        self.brand=brand
        self.model=model
        self.battery=battery
        self.storage=storage
    def charge(self,percent):
        if self.battery+percent <= 100:
            self.battery+=percent
        else: 
            self.battery=100
    def use(self,hours):
        self.battery=self.battery-(hours*10)
    def low_battery(self):
        if self.battery <=20:
            return True
        else:
            return False
    def display(self):
        return f"Brand:{self.brand} \n Model:{self.model} \n Battery:{self.battery} \n Storage:{self.storage}"
            
m1=Mobile("Redmi","Note 7", 45,128)
m1.charge(45)
m1.use(4)
print(m1.low_battery())
print(m1.display())
        
        