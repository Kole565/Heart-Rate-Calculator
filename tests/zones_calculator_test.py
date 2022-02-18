import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

import unittest

from lib.zones_calculator import ZonesCalculator


class TestZonesCalculator(unittest.TestCase):

    def setUp(self):
        age = 20
        rest_heart_rate = 60

        self.calc = ZonesCalculator(age, rest_heart_rate)
    
    def test_init(self):
        self.assertTrue(self.calc)
    
    def test_init_attrs(self):
        self.assertTrue(self.calc.max_hr)
        self.assertTrue(self.calc.rest_hr)
        self.assertTrue(self.calc.zones)
    
    def test_zones(self):
        self.assertEqual(len(self.calc.zones), 5)
    
    def test_get_zone(self):
        self.assertEqual(self.calc.get_zone("VO2").name, "VO2")
        self.assertEqual(self.calc.get_zone("Aero").name, "Aero")
        