def sorting():
    list1=[8,2,5]
    temp=[]
  
    
    for x in range(len(list1)):
        count=0 #because we need to return count to zero whenever it iterates
        for i in range (len(list1)):
            if(list1[i]<list1[x]):
                count+=1
        temp.append(count)
    print(temp)
sorting()    









