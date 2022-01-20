import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

import unittest

from lib.pulse import *


class TestMaxPulse(unittest.TestCase):

    def test_max_heart_rate(self):
        self.assertEqual(max_heart_rate(10), 199)
        self.assertEqual(max_heart_rate(50), 172)

    def test_max_heart_rate_invalid_age(self):
        try:
            max_heart_rate(0)
        except AssertionError:
            pass
        else:
            self.fail()
        
        try:
            max_heart_rate(101)
        except AssertionError:
            pass
        else:
            self.fail()
    
    def test_pulse_zone_invalid_data(self):
        try:
            pulse_zone(0, 0, 150, 60)
        except AssertionError:
            pass
        
        try:
            pulse_zone(120, 0, 150, 60)
        except AssertionError:
            pass
        else:
            self.fail()
        
        try:
            pulse_zone(0, 120, 150, 60)
        except AssertionError:
            pass
        else:
            self.fail()
        
        try:
            pulse_zone(0, 0, 50, 60)
        except AssertionError:
            pass
        else:
            self.fail()
        
        try:
            pulse_zone(0, 0, 500, 60)
        except AssertionError:
            pass
        else:
            self.fail()
        
        try:
            pulse_zone(0, 0, 150, 0)
        except AssertionError:
            pass
        else:
            self.fail()
        
        try:
            pulse_zone(0, 0, 150, 200)
        except AssertionError:
            pass
        else:
            self.fail()

    def test_VO2_zone(self):
        self.assertEqual(VO2_zone(190, 60), (177, 190))
        self.assertEqual(VO2_zone(190, 30), (174, 190))

    def test_anaero_zone(self):
        self.assertEqual(anaero_zone(190, 60), (164, 177))
        self.assertEqual(anaero_zone(190, 30), (158, 174))

    def test_aero_zone(self):
        self.assertEqual(aero_zone(190, 60), (151, 164))
        self.assertEqual(aero_zone(190, 30), (142, 158))

    def test_call_burn_zone(self):
        self.assertEqual(call_burn_zone(190, 60), (138, 151))
        self.assertEqual(call_burn_zone(190, 30), (126, 142))

    def test_light_activity_zone(self):
        self.assertEqual(light_activity_zone(190, 60), (125, 138))
        self.assertEqual(light_activity_zone(190, 30), (110, 126))
        