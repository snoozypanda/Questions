list1=[12,0,6,8,0]
temp1=[]
temp2=[]
for i in range(len(list1)):
    if list1[i]==0:
        temp1.append(list1[i])
    else:
        temp2.append(list1[i])
print (temp2+temp1)            