import random
import string

passw = []

a = string.ascii_uppercase
A = string.ascii_lowercase


s = ["@" , "#" , "$",  "%" , "&" , "_" , "?" ]


for i in range(2,8):
    a1 = random.choice(A)
    passw.append(a1)
for n in range(8):
    a2 = random.choice(a)
    passw.append(a2)
for m in range(3):
    s1 = random.choices(s)
    kl = random.randint(3,12)
    s2 = ''.join(s1)
    passw.insert( kl , s2)
for j in range(4,11):
    nu = random.randint(1,9)
    kt = random.randint(3 , 20)
    passw.insert( kt , str(nu))

print(passw)
values = ''.join(str(v) for v in passw)
print(values)


