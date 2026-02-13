class Point:
    points = []

    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = x
        self.y = y
        Point.points.append(self)

    def distance_to_origin(self) -> int | float:
        deltax = self.x
        deltay = self.y
        distance = ((deltax ** 2) + (deltay ** 2)) ** (1 / 2)
        return round(distance, 2)

    def distance_to_point(self, point: Point) -> int | float:
        deltax = self.x - point.x
        deltay = self.y - point.y
        distance = ((deltax ** 2) + (deltay ** 2)) ** (1 / 2)
        return round(distance, 2)

    def distance_to_x_axis(self) -> int | float:
        return abs(self.y)

    def distance_to_y_axis(self) -> int | float:
        return abs(self.x)

    def find_closest_point(self) -> None | int | float:
        if len(Point.points) <= 1:
            return None
        else:
            other_points = [point for point in Point.points if point != self]
            closest_distance = other_points[0].distance_to_point(self)
            closest_point = other_points[0]
            for point in other_points:
                if point.distance_to_point(self) < closest_distance:
                    closest_point = point
                    closest_distance = point.distance_to_point(self)
                else:
                    pass
            return closest_point
