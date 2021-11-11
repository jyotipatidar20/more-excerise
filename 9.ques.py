sentence = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system"
a=[]
b=''
for i in sentence:
    if i == ' ':
        a.append(b)
        b = ' '
    else:
        b +=i
if b:
    a.append(b)
print(a)






# list_1=sentence.split()
# print(list_1)

