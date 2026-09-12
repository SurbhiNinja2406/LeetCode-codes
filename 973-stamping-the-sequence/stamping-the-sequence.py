class Solution(object):
    def movesToStamp(self, stamp, target):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        """
        M, N = len(stamp), len(target)
        A = []
        for i in range(N - M + 1):
            made, todo = set(), set()
            for j, c in enumerate(stamp):
                a = target[i + j]
                if a == c:
                    made.add(i + j)
                else:
                    todo.add(i + j)
            A.append((made, todo))
        ans = []
        done = set()  
        while len(done) < N:
            did_stamp = False
            for i, (made, todo) in enumerate(A):
                if not todo and made:
                    did_stamp = True
                    ans.append(i)
                    for global_index in made:
                        done.add(global_index)
                        for i2, (made2, todo2) in enumerate(A):
                            todo2.discard(global_index)
                    A[i] = (set(), set())
            if not did_stamp:
                return []
        return ans[::-1]
if __name__ == "__main__":
    sol = Solution()
    print(sol.movesToStamp("abc", "ababc"))  
    print(sol.movesToStamp("abca", "aabcaca")) 
print(__name__)