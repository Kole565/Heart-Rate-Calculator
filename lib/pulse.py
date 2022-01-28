"""Pulse

Provide methods for pulse calculations.

"""


def max_heart_rate(age):
    """Get years; return decimal - max pulse."""
    assert age > 0, "Years should be more 0"
    assert age <= 100, "Years should be less or equal 100"

    rate = 205.8 - (0.685 * age)

    return round(rate)

def pulse_zone(lower, upper, max_hr, rest_hr):
    """Calculate pulse zone by lower, upper limit, max_hr in percents
    
    Get lower, upper; return (decimal, decimal) - pulse zone.

    """
    assert 0 <= lower <= 100, "Lower should be percent"
    assert 0 <= upper <= 100, "Upper should be percent"

    assert 100 <= max_hr <= 300, "Max heart rate should be valid"
    assert 20 <= rest_hr <= 120, "Rest heart rate should be valid"


    zone_lower = round(((max_hr - rest_hr) * lower / 100) + rest_hr)
    zone_upper = round(((max_hr - rest_hr) * upper / 100) + rest_hr)


    return (zone_lower, zone_upper)

def VO2_zone(max_hr, rest_hr):
    return pulse_zone(90, 100, max_hr, rest_hr)

def anaero_zone(max_hr, rest_hr):
    return pulse_zone(80, 90, max_hr, rest_hr)

def aero_zone(max_hr, rest_hr):
    return pulse_zone(70, 80, max_hr, rest_hr)

def call_burn_zone(max_hr, rest_hr):
    return pulse_zone(60, 70, max_hr, rest_hr)

def light_activity_zone(max_hr, rest_hr):
    return pulse_zone(50, 60, max_hr, rest_hr)


ZONES = [
    "VO2",
    "Anaero",
    "Aero",
    "Call Burn",
    "Light Activity",
]
ZONES_FUNC = [
    VO2_zone,
    anaero_zone,
    aero_zone,
    call_burn_zone,
    light_activity_zone,
]
