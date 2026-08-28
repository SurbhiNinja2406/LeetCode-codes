class MyHashMap(object):
    def __init__(self):
        self.num_buckets = 1000
        self.buckets = [[] for _ in range(self.num_buckets)]
    def _hash(self, key):
        return key % self.num_buckets
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = [key, value]  
                return
        bucket.append([key, value])  
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for k, v in bucket:
            if k == key:
                return v
        return -1 
    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
if __name__ == "__main__":
    myHashMap = MyHashMap()
    myHashMap.put(1, 1)           
    myHashMap.put(2, 2)         
    print(myHashMap.get(1))        
    print(myHashMap.get(3))       
    myHashMap.put(2, 1)           
    print(myHashMap.get(2))         
    myHashMap.remove(2)            
    print(myHashMap.get(2))      
print(__name__)