class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        if not tokens:
            return 0
        tokens.sort()
        left, right = 0, len(tokens) - 1
        score = 0
        max_score = 0
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
                max_score = max(max_score, score)
            elif score > 0:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break
        return max_score
if __name__ == "__main__":
    sol = Solution()
    print(sol.bagOfTokensScore([100], 50)) 
    print(sol.bagOfTokensScore([200, 100], 150)) 
    print(sol.bagOfTokensScore([100, 200, 300, 400], 200)) 
print(__name__)