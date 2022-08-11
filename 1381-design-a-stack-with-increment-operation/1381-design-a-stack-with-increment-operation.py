class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize=maxSize
        self.size=0
        self.st=[]

    def push(self, x: int) -> None:
        if self.size!=self.maxSize:
            self.st.append(x)
            self.size+=1

    def pop(self) -> int:
        if self.st:
            self.size-=1
            return self.st.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        if len(self.st)<=k:
            for i in range(len(self.st)):
                self.st[i]+=val
        else:
            for i in range(k):
                self.st[i]+=val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)