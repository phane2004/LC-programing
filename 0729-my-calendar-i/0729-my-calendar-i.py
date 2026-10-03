class MyCalendar:

    def __init__(self):
        self.cal = []        

    def book(self, startTime: int, endTime: int) -> bool:
        for st, en in self.cal:
            if en > startTime and st < endTime:
                return False
        self.cal.append([startTime, endTime])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)