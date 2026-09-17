class Solution(object):
    def videoStitching(self, clips, time):
        """
        :type clips: List[List[int]]
        :type time: int
        :rtype: int
        """
        clips.sort()
        count = 0
        current_end = 0   
        farthest = 0      
        i = 0
        n = len(clips)
        while current_end < time:
            while i < n and clips[i][0] <= current_end:
                farthest = max(farthest, clips[i][1])
                i += 1
            if farthest <= current_end:
                return -1
            count += 1
            current_end = farthest
        return count
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], 10, 3),
        ([[0, 1], [1, 2]], 5, -1),
        ([[0, 1], [6, 8], [0, 2], [5, 6], [0, 4], [0, 3], [6, 7],
          [1, 3], [4, 7], [1, 4], [2, 5], [2, 6], [3, 4], [4, 5],
          [5, 7], [6, 9]], 9, 3),
        ([[0, 4], [2, 8]], 5, 1),
        ([[0, 4]], 4, 1),
    ]
    for clips, time, expected in test_cases:
        clips_copy = [c[:] for c in clips]
        result = sol.videoStitching(clips_copy, time)
        status = "PASS" if result == expected else "FAIL"
        print("clips={0}, time={1} -> {2} (expected {3}) [{4}]".format(
            clips, time, result, expected, status
        ))
print(__name__)