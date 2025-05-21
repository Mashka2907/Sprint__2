class PointsForPlace:
    """Вычисляет очки в зависимости от места, которое занял спортсмен."""

    def __init__(self):
        self.points = 0

    def get_points_for_place(self, place):
        if place > 100:
            return 'Баллы начисляются только первым 100 участникам'
        elif place < 1:
            return 'Спортсмен не может занять нулевое или отрицательное место'
        else:
            self.points = 101 - place
            return self.points

class PointsForMeters:

    """Вычисляет очки в зависимости от количества метров, на которое спортсмен толкнул ядро или метнул диск"""
    def __init__(self):
        self.points = 0

    def get_points_for_meters(self, meters):
        if meters < 0:
            return 'Количество метров не может быть отрицательным'
        else:
            self.points = meters * 0.5
            return self.points

class TotalPoints(PointsForPlace, PointsForMeters):
    """Вычисляет общую сумму очков, складывая очки за место и очки за метры"""

    def get_total_points(self, meters, place):
        total = self.get_points_for_place(place) + self.get_points_for_meters(meters)
        return total


points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))