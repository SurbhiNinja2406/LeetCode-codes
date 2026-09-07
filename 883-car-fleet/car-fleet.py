class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        n = len(position)
        if n == 0:
            return 0
        cars = sorted(zip(position, speed), key=lambda x: -x[0])
        fleets = 0
        prev_time_to_target = 0.0
        for pos, spd in cars:
            time_to_target = (target - pos) / float(spd)
            if time_to_target > prev_time_to_target:
                fleets += 1
                prev_time_to_target = time_to_target
        return fleets
if __name__ == "__main__":
    solution = Solution()
    target1 = 12
    position1 = [10, 8, 0, 5, 3]
    speed1 = [2, 4, 1, 1, 3]
    print(solution.carFleet(target1, position1, speed1))  
    target2 = 10
    position2 = [3]
    speed2 = [3]
    print(solution.carFleet(target2, position2, speed2))  
    target3 = 100
    position3 = [0, 2, 4]
    speed3 = [4, 2, 1]
    print(solution.carFleet(target3, position3, speed3)) 
    target4 = 10
    position4 = [0, 4, 8]
    speed4 = [1, 2, 3]
    print(solution.carFleet(target4, position4, speed4))
    target5 = 20
    position5 = [10, 15]
    speed5 = [2, 3]
    print(solution.carFleet(target5, position5, speed5))
print(__name__)