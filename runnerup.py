if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr1=list(set(arr))
    arr1.sort(reverse=True)
    print(arr1[1])