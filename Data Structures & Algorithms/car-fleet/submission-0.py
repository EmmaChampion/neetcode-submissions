class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carData = {}
        for i in range(len(position)):
            carData[position[i]] = speed[i]
        carData = dict(sorted(carData.items(), reverse=True))

        fleets = []
        for position, speed in carData.items():
            time = (target - position) / speed
            if len(fleets) == 0:
                fleets.append(time)
            elif time > fleets[-1]:
                fleets.append(time)
        
        return len(fleets)