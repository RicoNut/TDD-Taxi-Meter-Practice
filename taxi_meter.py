# -*- coding: utf-8 -*-


class TaxiMeter(object):
    def __init__(self):
        self.cash = 0
        self.start_time = None
        self.end_time = None

    def start(self, start_time):
        self.start_time = float(start_time)

    def receive(self, current_time, miles):
        print "miles: {0}".format(miles)
        if miles > 3:
            self.cash = 14 + (miles - 3) * 2.4
        else:
            self.cash = 14
