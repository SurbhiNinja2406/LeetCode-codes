from collections import Counter
class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        n = len(hand)
        if n % groupSize != 0:
            return False
        count = Counter(hand)
        sorted_cards = sorted(count.keys())
        for card in sorted_cards:
            if count[card] == 0:
                continue  
            needed = count[card]  
            for next_card in range(card, card + groupSize):
                if count[next_card] < needed:
                    return False  
                count[next_card] -= needed
        return True
if __name__ == "__main__":
    solution = Solution()
    hand1, groupSize1 = [1, 2, 3, 6, 2, 3, 4, 7, 8], 3
    print(solution.isNStraightHand(hand1, groupSize1))  
    hand2, groupSize2 = [1, 2, 3, 4, 5], 4
    print(solution.isNStraightHand(hand2, groupSize2))  
    hand3, groupSize3 = [1, 1, 2, 2, 3, 3], 1
    print(solution.isNStraightHand(hand3, groupSize3))  
    hand4, groupSize4 = [1, 2, 3], 3
    print(solution.isNStraightHand(hand4, groupSize4)) 
    hand5, groupSize5 = [1, 2, 3, 4], 3
    print(solution.isNStraightHand(hand5, groupSize5))  
    hand6, groupSize6 = [1, 2, 3, 1, 2, 3, 4, 5, 6], 3
    print(solution.isNStraightHand(hand6, groupSize6))  
print(__name__)