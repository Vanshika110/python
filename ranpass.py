import random 
import string

len=8
char=string.ascii_letters+string.digits+string.punctuation
res="".join(random.choice(char) for i in range(len))
password=res
"""password=""
for i in range(len):
    password+=random.choice(char)"""

print("your random password is "+password)