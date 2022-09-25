class MyCircularQueue:

    def __init__(self, k: int):
        self.k=k
        self.q=[0]*k
        self.s=0
        self.f=0

    def enQueue(self, value: int) -> bool:
        if self.s==self.k:
            return False
        self.q[(self.f+self.s)%self.k]=value
        self.s+=1
        return True

    def deQueue(self) -> bool:
        if self.s==0:
            return False
        self.f=(self.f+1)%self.k
        self.s-=1
        return True
            
    def Front(self) -> int:
        if self.s:
            return self.q[self.f]
        return -1

    def Rear(self) -> int:
        if self.s:
            return self.q[(self.f+self.s-1)%self.k]
        return -1

    def isEmpty(self) -> bool:
        return self.s==0

    def isFull(self) -> bool:
        return self.s==self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()