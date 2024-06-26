import random

import string

pass_len=12
charvalue=string.ascii_letters+string.digits+string.punctuation

password=""
for i in range(pass_len):
    password += random.choice(charvalue)

#list comprehension password="".join([random.choice(charvalue) for i in range(pass_len)])
#print(res)    
print("your random password is: ", password)
