class TwoSum(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counts = {}
    def add(self, number):
        """
        Adds number to the data structure.
        :type number: int
        :rtype: None
        """
        self.counts[number] = self.counts.get(number, 0) + 1
    def find(self, value):
        for num in self.counts:
            complement = value - num
            if complement == num:
                if self.counts[num] >= 2:
                    return True
            else:
                if complement in self.counts:
                    return True
        return False
if __name__ == "__main__":
    twoSum = TwoSum()
    twoSum.add(1)  
    twoSum.add(3)  
    twoSum.add(5)  
    result1 = twoSum.find(4)  
    result2 = twoSum.find(7)  
    print("[{0}] find(4) -> got {1}, expected True".format(
        "PASS" if result1 == True else "FAIL", result1
    ))
    print("[{0}] find(7) -> got {1}, expected False".format(
        "PASS" if result2 == False else "FAIL", result2
    ))
    twoSum2 = TwoSum()
    twoSum2.add(3)
    twoSum2.add(3)
    result3 = twoSum2.find(6) 
    print("[{0}] find(6) after adding 3 twice -> got {1}, expected True".format(
        "PASS" if result3 == True else "FAIL", result3
    ))
    twoSum3 = TwoSum()
    twoSum3.add(3)
    result4 = twoSum3.find(6)  
    print("[{0}] find(6) after adding 3 once -> got {1}, expected False".format(
        "PASS" if result4 == False else "FAIL", result4
    ))
    twoSum4 = TwoSum()
    twoSum4.add(-1)
    twoSum4.add(5)
    result5 = twoSum4.find(4) 
    print("[{0}] find(4) with -1 and 5 -> got {1}, expected True".format(
        "PASS" if result5 == True else "FAIL", result5
    ))
    twoSum5 = TwoSum()
    result6 = twoSum5.find(0)  
    print("[{0}] find(0) with empty structure -> got {1}, expected False".format(
        "PASS" if result6 == False else "FAIL", result6
    ))
print(__name__)
# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)