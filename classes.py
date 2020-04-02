#!/usr/bin/env python
from time import sleep

class Pause():
    def __init__(self):
        pass
    def small(self):
        sleep(1)
    def medium(self):
        sleep(3)
    def large(self):
        sleep(5)
    def reset(self):
        sleep(120)