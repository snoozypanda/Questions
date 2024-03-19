list=[9]

temp=[]
n=len(list)

for i in range(n):

    if(i!=n-1):
        temp.append(list[i])
    else:
        list[i]+=1
        if(list[i]>9):
            num=list[i]
            n=num//10
            
            temp.append(n)
            a=num%10
            temp.append(a)
        else:
            temp.append(list[i])   

        


        
print(temp)              
    


