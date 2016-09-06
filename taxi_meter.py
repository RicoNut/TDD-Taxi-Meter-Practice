# -*- coding: utf-8 -*-


class TaxiMeter():
    def __init__(self):
        self.cash = 0
        self.start_time = None
        self.end_time = None

    def start(self, start_time):
        self.start_time = float(start_time)

    def receive(self, current_time, miles):
        self.cash = 14
