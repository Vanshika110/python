"""class Acc:
    def __init__(self,bal,info):
        self.bal=bal
        self.info=info

    def debit(self,amount):
        self.bal-=amount
        print("debited", amount)

    def credit(self,amount):
        self.bal+=amount
        print("credited", amount)

    def print(self):
        return self.bal
    
    def __pri(): #private
        print("hello")
    
    def hello(self):
        self.__pri

    

a1=Acc(1000000,12345)
a2=Acc(299,44)
print(a1.hello())
print(a2)
del a2
a1.debit(10000)
a1.credit(50000)
print("Balance=",a1.print())  """


class Circle: 
    def __init__(self,r) :
        self.r=r

    def area(self,r):
        ar=3.14*self.r*self.r
        print(ar)

    def peri(self,r):
        pe=3.14*2*self.r
        print(pe)
c1=Circle(12)
c1.area(12)
c1.peri(12)