def lastIndex(arr,i,t):
    if i==len(arr):
        return -1
    ind = lastIndex(arr,i+1,t)
    if ind == -1:
        if arr[i]==t:
            return i 
        else:
            return -1
    else:
        return ind
print(lastIndex([1,2,8,0,5,8,8],0,8))