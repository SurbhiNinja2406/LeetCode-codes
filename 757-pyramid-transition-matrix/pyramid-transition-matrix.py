from collections import defaultdict
class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        pair_to_tops = defaultdict(list)
        for pattern in allowed:
            left, right, top = pattern[0], pattern[1], pattern[2]
            pair_to_tops[left + right].append(top)
        def build(row):
            if len(row) == 1:
                return True
            next_rows = [""]
            for i in range(len(row) - 1):
                pair = row[i] + row[i + 1]
                if pair not in pair_to_tops:
                    return False 
                tops = pair_to_tops[pair]
                new_next_rows = []
                for partial in next_rows:
                    for t in tops:
                        new_next_rows.append(partial + t)
                next_rows = new_next_rows
            for candidate in next_rows:
                if build(candidate):
                    return True
            return False
        return build(bottom)
if __name__ == "__main__":
    sol = Solution()
    print(sol.pyramidTransition("BCD", ["BCC", "CDE", "CEA", "FFF"]))
    print(sol.pyramidTransition("AAAA", ["AAB", "AAC", "BCD", "BBE", "DEF"]))
print(__name__)