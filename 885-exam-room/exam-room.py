import bisect
class ExamRoom(object):
    def __init__(self, n):
        """
        :type n: int
        """
        self.n = n
        self.seats = [] 
    def seat(self):
        """
        :rtype: int
        """
        if not self.seats:
            chosen = 0
        else:
            best_dist = self.seats[0]  
            chosen = 0
            for i in range(1, len(self.seats)):
                left = self.seats[i - 1]
                right = self.seats[i]
                gap_dist = (right - left) // 2  
                if gap_dist > best_dist:
                    best_dist = gap_dist
                    chosen = left + gap_dist
            last_dist = self.n - 1 - self.seats[-1]
            if last_dist > best_dist:
                best_dist = last_dist
                chosen = self.n - 1
        bisect.insort(self.seats, chosen)
        return chosen
    def leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        idx = bisect.bisect_left(self.seats, p)
        if idx < len(self.seats) and self.seats[idx] == p:
            self.seats.pop(idx)
if __name__ == "__main__":
    examRoom = ExamRoom(10)
    print(None)      
    print(examRoom.seat())  
    print(examRoom.seat())  
    print(examRoom.seat())  
    print(examRoom.seat())  
    examRoom.leave(4)
    print(None)        
    print(examRoom.seat())  
    print("---")
    examRoom2 = ExamRoom(4)
    print(examRoom2.seat())  
    print(examRoom2.seat())
    print(examRoom2.seat()) 
    print(examRoom2.seat())  
    print("---")
    examRoom3 = ExamRoom(5)
    print(examRoom3.seat())  
    print(examRoom3.seat()) 
    print(examRoom3.seat()) 
    examRoom3.leave(0)
    print(examRoom3.seat())  
print(__name__)
# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)