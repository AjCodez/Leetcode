class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                if 2*arr[i]==arr[j] or 2*arr[j]==arr[i]:
                    return True
        return False