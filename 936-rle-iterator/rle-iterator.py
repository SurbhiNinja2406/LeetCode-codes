class RLEIterator(object):
    def __init__(self, encoding):
        """
        :type encoding: List[int]
        """
        self.encoding = encoding
        self.index = 0  
    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        while self.index < len(self.encoding):
            count = self.encoding[self.index]
            value = self.encoding[self.index + 1]
            if n <= count:
                self.encoding[self.index] -= n
                return value
            else:
                n -= count
                self.index += 2
        return -1
if __name__ == "__main__":
    ops = ["RLEIterator", "next", "next", "next", "next"]
    args = [[[3, 8, 0, 9, 2, 5]], [2], [1], [1], [2]]
    output = []
    rLEIterator = None
    for op, arg in zip(ops, args):
        if op == "RLEIterator":
            rLEIterator = RLEIterator(*arg)
            output.append(None)
        elif op == "next":
            output.append(rLEIterator.next(*arg))
    print("Example 1:")
    print("Input: ")
    print(ops)
    print(args)
    print("Output:", output)
print(__name__)
# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)