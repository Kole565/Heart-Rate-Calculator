from heart_rate_zone import HeartRateZone


class ZonesCalculator:

    """Provide methods for pulse zones calculation."""

    def __init__(self, age, rest_heart_rate):
        self.check_age(age)
        self.check_rest_heart_rate(rest_heart_rate)

        self.max_hr = self.get_max_heart_rate(age)
        self.rest_hr = rest_heart_rate

        self.init_zones()
    
    def check_age(self, age):
        assert age > 0, "Years should be more 0"
        assert age <= 100, "Years should be less or equal 100"
    
    def check_rest_heart_rate(self, rest_hr):
        assert 20 <= rest_hr <= 120, "Rest heart rate should be between 20, 120"
    
    def get_max_heart_rate(self, age):
        """Get years; return decimal - max pulse."""
        assert age > 0, "Years should be more 0"
        assert age <= 100, "Years should be less or equal 100"

        rate = 205.8 - (0.685 * age)

        return round(rate)
    
    def init_zones(self):
        self.zones = [
            HeartRateZone("Light Activity", self.max_hr, self.rest_hr, 50, 60),
            HeartRateZone("Call Burn", self.max_hr, self.rest_hr, 60, 70),
            HeartRateZone("Aero", self.max_hr, self.rest_hr, 70, 80),
            HeartRateZone("Anaero", self.max_hr, self.rest_hr, 80, 90),
            HeartRateZone("VO2", self.max_hr, self.rest_hr, 90, 100)
        ]
    
    def get_zone(self, name):
        return [zone for zone in self.zones if zone.name == name][0]
