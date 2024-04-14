list1 = [1, 2, 4, 6, 9, 7]
target = 9
left = 0
right = len(list1) - 1

while left <= right:
    mid = (right + left) // 2
    if list1[mid] == target:
        print(mid)
        break
    elif target > list1[mid]:
        left = mid + 1
    else:
        right = mid - 1


