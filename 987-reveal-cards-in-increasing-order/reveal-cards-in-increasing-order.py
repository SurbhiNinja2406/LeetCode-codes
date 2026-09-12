from collections import deque
class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        n = len(deck)
        deck.sort()
        index_queue = deque(range(n))
        result = [0] * n
        for card in deck:
            reveal_index = index_queue.popleft()
            result[reveal_index] = card
            if index_queue:
                index_queue.append(index_queue.popleft())
        return result
if __name__ == "__main__":
    sol = Solution()
    print(sol.deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]))
    print(sol.deckRevealedIncreasing([1, 1000]))
print(__name__)