list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
i=0
a=[]
for i in list1:
    if i not  in  a:
        a.append(i)
for j in list2:
    if j not in  a:
        a.append(j)
print(a)

    




    