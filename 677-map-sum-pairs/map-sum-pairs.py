class MapSum(object):
    def __init__(self):
        self.map = {}
    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        self.map[key] = val
    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        total = 0
        for key, val in self.map.items():
            if key.startswith(prefix):
                total += val
        return total
if __name__ == "__main__":
    mapSum = MapSum()
    mapSum.insert("apple", 3)
    print('insert("apple", 3) -> None')
    r1 = mapSum.sum("ap")
    print('sum("ap"):', r1, '| Expected: 3') 
    mapSum.insert("app", 2)
    print('insert("app", 2) -> None')
    r2 = mapSum.sum("ap")
    print('sum("ap"):', r2, '| Expected: 5')  
    print()
    mapSum2 = MapSum()
    mapSum2.insert("apple", 3)
    mapSum2.insert("apple", 10)  
    r3 = mapSum2.sum("apple")
    print('Override test - sum("apple"):', r3, '| Expected: 10')
    r4 = mapSum2.sum("banana")
    print('No match - sum("banana"):', r4, '| Expected: 0')
    mapSum2.insert("app", 1)
    mapSum2.insert("apricot", 5)
    r5 = mapSum2.sum("ap")
    print('Multiple matches - sum("ap"):', r5, '| Expected: 16')  
print(__name__)
# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)