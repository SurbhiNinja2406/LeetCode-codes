from collections import defaultdict
class FreqStack(object):
    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.max_freq = 0
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_freq = self.freq[val] + 1
        self.freq[val] = new_freq
        if new_freq > self.max_freq:
            self.max_freq = new_freq
        self.group[new_freq].append(val)
    def pop(self):
        """
        :rtype: int
        """
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return val
if __name__ == "__main__":
    operations = ["FreqStack", "push", "push", "push", "push", "push", "push",
                  "pop", "pop", "pop", "pop"]
    args = [[], [5], [7], [5], [7], [4], [5], [], [], [], []]
    output = []
    freqStack = None
    for op, arg in zip(operations, args):
        if op == "FreqStack":
            freqStack = FreqStack()
            output.append(None)
        elif op == "push":
            freqStack.push(arg[0])
            output.append(None)
        elif op == "pop":
            result = freqStack.pop()
            output.append(result)

    print("Output: {}".format(output))
    print("Expected: [None, None, None, None, None, None, None, 5, 7, 5, 4]")
print(__name__)
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()