class Solution:
    def maximum69Number (self, num: int):
        num=str(num)
        for i in range(len(num)):
            if num[i]=='6':
                num=num[:i]+'9'+num[i+1:]
                return num
        return num