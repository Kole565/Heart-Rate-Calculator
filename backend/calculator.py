from .exceptions import *


class Calculator:

    ZONES_COEFFICIENTS = [
        [0.5, 0.7],
        [0.7, 0.8],
        [0.8, 0.87],
        [0.87, 0.94],
        [0.94, 1],
    ]

    def __init__(self, age, rest_hr):
        self.zones = []

        self.calculate(age, rest_hr)

    def calculate(self, age, rest_hr):
        self._age = age
        self._rest_hr = rest_hr

        self._validate_input(age, rest_hr)
        self._calculate_zones(age, rest_hr)

        return self.zones

    def _validate_input(self, age, rest_hr):
        if (age < 16 or age > 120):
            raise InvalidInput

        if (rest_hr < 20 or rest_hr > 120):
            raise InvalidInput

    def _calculate_zones(self, age, rest_hr):
        if (self._age, self._rest_hr) == (age, rest_hr) and self.zones:
            return

        self.zones = []

        max_hr = 207 - 0.7 * age
        for lower, upper in self.ZONES_COEFFICIENTS:
            self.zones.append([
                round(lower * (max_hr - rest_hr) + rest_hr, 2),
                round(upper * (max_hr - rest_hr) + rest_hr, 2)
            ])
