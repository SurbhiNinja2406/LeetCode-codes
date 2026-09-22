class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        """
        :type req_skills: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
        n = len(req_skills)
        skill_to_index = {skill: i for i, skill in enumerate(req_skills)}
        people_masks = []
        for person_skills in people:
            mask = 0
            for skill in person_skills:
                if skill in skill_to_index:
                    mask |= (1 << skill_to_index[skill])
            people_masks.append(mask)        
        full_mask = (1 << n) - 1
        dp = {0: []}        
        for person_idx, person_mask in enumerate(people_masks):
            for mask, team in list(dp.items()):
                new_mask = mask | person_mask                
                if new_mask == mask:
                    continue                
                new_team = team + [person_idx]
                if new_mask not in dp or len(new_team) < len(dp[new_mask]):
                    dp[new_mask] = new_team        
        return dp[full_mask]
if __name__ == "__main__":
    solution = Solution()
    req_skills1 = ["java", "nodejs", "reactjs"]
    people1 = [["java"], ["nodejs"], ["nodejs", "reactjs"]]
    result1 = solution.smallestSufficientTeam(req_skills1, people1)
    print("Example 1: {} (Expected: [0,2] or equivalent minimal team)".format(result1))
    req_skills2 = ["algorithms", "math", "java", "reactjs", "csharp", "aws"]
    people2 = [
        ["algorithms", "math", "java"],
        ["algorithms", "math", "reactjs"],
        ["java", "csharp", "aws"],
        ["reactjs", "csharp"],
        ["csharp", "math"],
        ["aws", "java"]
    ]
    result2 = solution.smallestSufficientTeam(req_skills2, people2)
    print("Example 2: {} (Expected: [1,2] or equivalent minimal team)".format(result2))
print(__name__)