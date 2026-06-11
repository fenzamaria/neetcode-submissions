class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = list(zip(position, speed))

        cars.sort(reverse=True)

        fleets = 0
        lastTime = 0

        for pos, spd in cars:

            time = (target - pos) / spd

            if time > lastTime:
                fleets += 1
                lastTime = time

        return fleets