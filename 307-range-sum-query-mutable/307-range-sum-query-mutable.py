class NumArray:
    
    arr=[]
    tsum = 0

    def __init__(self, nums: List[int]):
        self.arr = nums
        self.tsum = sum(nums)

    def update(self, index: int, val: int) -> None:
        
        self.tsum = self.tsum - self.arr[index]
        self.arr[index] = val
        self.tsum = self.tsum + self.arr[index]
        

    def sumRange(self, left: int, right: int) -> int:
        
        ans = self.tsum
        
        for i in range(0,left):
            ans = ans - self.arr[i]
        for i in range(right+1,len(self.arr)):
            ans = ans - self.arr[i]
        return ans


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)