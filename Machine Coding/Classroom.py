class Classroom:
    def __init__(self,class_name):
        self.class_name=class_name
        self.students=[]
        
    def addStudent(self,name):
        self.students.append(name)
    
    def removeStudent(self,name):
        self.students.remove(name)
    
    
    def total_Students(self):
        return len(self.students)
        
    def searchStudent(self,name):
        if name in self.students:
            return True
        else:
            return False
            
    def display(self):
        return f"Class:{self.class_name} \n Students: {self.students} "
        
        
c = Classroom("CSE-A")

c.addStudent("Aadhi")
c.addStudent("Rahul")
c.addStudent("Varun")

c.removeStudent("Rahul")

print(c.total_Students())

print(c.searchStudent("Aadhi"))

print(c.display())