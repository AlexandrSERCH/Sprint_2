class PointsForPlace:
    def __init__(self):
        self.place_points = 0

    def get_points_for_place(self, place: int):
        if place > 100:
            return 'Баллы начисляются только первым 100 участникам'
        elif place < 1:
            return 'Спортсмен не может занять нулевое или отрицательное место'
        else:
            self.place_points = 101 - place
            return self.place_points


class PointsForMeters:
    def __init__(self):
        self.meters_points = 0

    def get_points_for_meters(self, meters: int):
        if meters < 0:
            return 'Количество метров не может быть отрицательным'
        else:
            self.meters_points = meters * 0.5
            return self.meters_points

class TotalPoints(PointsForPlace, PointsForMeters):
    def __init__(self):
        PointsForPlace.__init__(self)
        PointsForMeters.__init__(self)

    def get_total_points(self, meters, place):
        total = self.get_points_for_meters(meters) + self.get_points_for_place(place)

        return total


points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))