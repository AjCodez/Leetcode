class MyCalendar:
    
    def __init__(self):
        self.booking = []

    def book(self, start: int, end: int) -> bool:
        if len(self.booking)==0:
            self.booking.append((start,end))
            return True
        for i in self.booking:
            if start>=i[0] and start<i[1]:
                return False
            if end>i[0] and end<=i[1]:
                return False
            if start<=i[0] and end>=i[1]:
                return False
        self.booking.append((start,end))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)