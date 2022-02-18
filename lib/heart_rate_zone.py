class HeartRateZone:
    
    
    def __init__(self, name, max_heart_rate, rest_heart_rate,
                                    lower_limit_percent, upper_limit_percent):
        self.name = name

        self.check_lower_percent(lower_limit_percent, upper_limit_percent)
        self.check_upper_percent(lower_limit_percent, upper_limit_percent)

        self.max_hr = max_heart_rate
        self.rest_hr = rest_heart_rate
        self.lower = self.get_heart_rate(lower_limit_percent)
        self.upper = self.get_heart_rate(upper_limit_percent)
    
    def check_lower_percent(self, lower, upper):
        assert 0 <= lower <= 100, "Lower should be percent"
        assert lower <= upper, "Lower should be less then upper"
    
    def check_upper_percent(self, lower, upper):
        assert 0 <= upper <= 100, "Upper should be percent"
        assert upper >= lower, "Upper should be more then lower"
    
    def get_heart_rate(self, percent):
        delta_hr = self.max_hr - self.rest_hr
        percent /= 100
        
        rate = delta_hr * percent + self.rest_hr
        rate = round(rate)

        return rate
        