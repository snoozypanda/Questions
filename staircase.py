#def steps(n):
    #if n>3:
       # return steps(n-1)+steps(n-2)
    #else:
       # return n
#print(steps(6))    
nums=[1,2,3,4] 
temp=[]
temp.append(nums[0])
for i in range(1,len(nums)+1):
    nums[i]=nums[0]+(nums[i]-1)
    temp.append(nums[i])
print(temp)    



