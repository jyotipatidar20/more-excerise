a="vaishnavi"
i=0
b=[]
while i<len(a):
    if type(a[i])==str:
            b.append(a[i]) 
    i=i+1
print(b)
print(len(b))
j=0
c=[]
d=[]
while j<len(a):
    if a[j]=="a" or a[j]=="e" or a[j]=="i" or a[j]=="o" or a[j]=="u":
        c.append(a[j])
    else:
        d.append(a[j])
    j=j+1
print(c)
print(len(c),"vowel")
print(d)
print(len(d),"consonant")