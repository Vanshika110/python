import os

f=open("sample.txt","wt")
f.write("hello everyone!! \n how are u all?")
f.close()


prob="lem"
with open("sample.txt","r") as f:
        data=f.read()
        new=data.replace("everyone","all")
        print(new)
        if(data.find(prob)!=1):
            print("found")
        else:
         print("not found")
        for x in f:
            print(x)
        print(f.read(5))
        print(f.readline())
    

        if os.path.exists("samle.txt"):
            os.remove("samle.txt")
        else:
            print("not exist")
