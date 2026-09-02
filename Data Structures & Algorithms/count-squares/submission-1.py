class CountSquares:

    def __init__(self):
        self.pointsCount = {}
        self.points = []

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        if point in self.pointsCount:
            self.pointsCount[point] += 1
        else:
            self.pointsCount[point] = 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        result = 0
        point = tuple(point)
        for corner in self.points:
            if corner[0] != point[0] and corner[1] != point[1] and abs(corner[0] - point[0]) == abs(corner[1] - point[1]):
                if (point[0], corner[1]) in self.pointsCount and (corner[0], point[1]) in self.pointsCount:
                    result += self.pointsCount[(point[0], corner[1])] * self.pointsCount[(corner[0], point[1])]
        return result