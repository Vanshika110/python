import random
tar=random.randint(1,100)
while True:
    num=input("enter num or quit")
    if(num=="quit"):
        break
    num=int(num)
    if(num==tar):
        print("correct ")
    elif(num>tar):
        print("guess less no.")
    else:
        print("guess big no.")
print("--game over--")
