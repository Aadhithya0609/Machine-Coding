class Book:
    def __init__(self,page,title,author,price):
        self.page=page
        self.title=title
        self.author=author
        self.price=price
        
    def discount(self,discount):
        self.discounts=self.price-(self.price* discount/100)
    def islongbook(self):
        if self.page >= 500:
            return True
        else:
            return False
    def display(self):
        return f"Title: {self.title} \n Author: {self.author}\n Price:{self.price} \n Discounted Price: {self.discounts}"
        
        
s1=Book(500,"Python Crash Course","Eric Matthes",650)
s1.discount(20)
print(s1.display())
print(s1.islongbook())

        