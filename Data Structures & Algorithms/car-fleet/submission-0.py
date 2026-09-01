class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(reverse=True)
        # t = x / s
        # x = distance traveled = target - pos
        last_time = 0
        fleets = 0
        for pos, spd in cars:
            time = (target - pos) / spd
            if time > last_time:
                last_time = time
                fleets+=1
        return fleets

        
        return fleets