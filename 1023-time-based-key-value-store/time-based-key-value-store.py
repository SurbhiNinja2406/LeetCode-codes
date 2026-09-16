from collections import defaultdict
import bisect
class TimeMap(object):
    def __init__(self):
        self.timestamps = defaultdict(list)
        self.values = defaultdict(list)
    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.timestamps[key].append(timestamp)
        self.values[key].append(value)
    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.timestamps:
            return ""
        ts_list = self.timestamps[key]
        idx = bisect.bisect_right(ts_list, timestamp)
        if idx == 0:
            return ""
        return self.values[key][idx - 1]
if __name__ == "__main__":
    timeMap = TimeMap()
    timeMap.set("foo", "bar", 1)
    print(timeMap.get("foo", 1))   
    print(timeMap.get("foo", 3))  
    timeMap.set("foo", "bar2", 4)
    print(timeMap.get("foo", 4))  
    print(timeMap.get("foo", 5))  
print(__name__)
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)