# -*- coding: utf-8 -*-

import unittest


class TaxiMeterTestCase(unittest.TestCase):

    def setUp(self):
        self.taxi_meter = TaxiMeter()
        pass

    def tearDown(self):
        pass

    # @unittest.skip('')
    def test_mile_lt_3_normal_time(self):
        self.taxi_meter.start('6:00')
        self.taxi_meter.receive('7:00', 2)
        self.assertEqual(self.taxi_meter.cash, 14)


if __name__ == '__main__':
    unittest.main()