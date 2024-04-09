class Student:
    def __init__(self,name,marks):
     self.name=name
     self.marks=marks

    @staticmethod
    def hello():
       print("hello")

    def avg(self):
       sum=0
       for val in self.marks:
          sum+=val
       print("avg score of",self.name,sum/3)

    s1 = Student("vanshii",[96,99,98])
    s1.avg()
    s1.name="priya"
    s1.avg() 
    
