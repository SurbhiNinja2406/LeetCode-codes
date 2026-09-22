class Solution(object):
    def sampleStats(self, count):
        """
        :type count: List[int]
        :rtype: List[float]
        """
        minimum = -1
        maximum = -1
        total_sum = 0
        total_count = 0
        mode = 0
        max_freq = 0
        
        # Single pass to find minimum, maximum, sum, total count, and mode
        for value in range(256):
            freq = count[value]
            if freq == 0:
                continue
            
            if minimum == -1:
                minimum = value
            maximum = value
            
            total_sum += value * freq
            total_count += freq
            
            if freq > max_freq:
                max_freq = freq
                mode = value
        
        mean = float(total_sum) / total_count
        
        # Find the median by walking through counts in order
        median = 0.0
        if total_count % 2 == 1:
            # Odd number of elements: find the single middle element
            target = total_count // 2 + 1
            running = 0
            for value in range(256):
                running += count[value]
                if running >= target:
                    median = float(value)
                    break
        else:
            # Even number of elements: average the two middle elements
            target1 = total_count // 2
            target2 = total_count // 2 + 1
            val1 = -1
            val2 = -1
            running = 0
            for value in range(256):
                running += count[value]
                if val1 == -1 and running >= target1:
                    val1 = value
                if running >= target2:
                    val2 = value
                    break
            median = (val1 + val2) / 2.0        
        return [float(minimum), float(maximum), mean, median, float(mode)]
if __name__ == "__main__":
    solution = Solution()
    count1 = [0] * 256
    count1[1] = 1
    count1[2] = 2
    count1[3] = 3
    result1 = solution.sampleStats(count1)
    print("Example 1: {} (Expected: [1.0, 3.0, 2.375, 2.5, 3.0])".format(result1))
    count2 = [0] * 256
    count2[1] = 4
    count2[2] = 3
    count2[3] = 2
    count2[4] = 2
    result2 = solution.sampleStats(count2)
    print("Example 2: {} (Expected: [1.0, 4.0, 2.18182, 2.0, 1.0])".format(result2))
print(__name__)