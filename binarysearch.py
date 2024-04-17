list1 = [5, 6, 8, 12, 15, 21, 25, 31]
target = 25
left = 0
right = len(list1) - 1

while left <= right:
    mid = (right + left) // 2
    if list1[mid] == target:
        print( mid)
        break
    elif target > list1[mid]:
        left = mid + 1
    elif target<list1[mid]:
        right = mid - 1
    else:
        print("There is nothing")


   
