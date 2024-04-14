list1=[7,4,5,9]
highestnumber=0
second=0
for i in range(len(list1)):
    
         
        if list1[i] > highest_number:
        
            highestnumber=list[i]
            

        else:
            continue
for i in range (len(list1)):
    if(list1[i]==highestnumber):
        list1.remove(i)
for i in range (len(list1)):
    if(list[i]>second):
        a_z = 'abcdefghijklmnopqrstuvwxyz'
pasw = 'dog'
tests = 0
guess = ''
azlen = len(a_z)

for i in range(azlen):
    for j in range(azlen):
        for k in range(azlen):
            guess = a_z[i] + a_z[j] + a_z[k]
            tests += 1
            if guess == pasw:
                print('Got "{}" after {} tests'.format(guess, str(tests)))
                break

input()





        
    
       





