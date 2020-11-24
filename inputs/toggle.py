"""
Use an input when you need to normalize the input range (e.g. analog sensor). Call the set() method
with a value in range vmin-vmax. The get() method will return a value in range 0-1.
"""
from utils.boolean import Boolean


class Toggle(Boolean):
    def __init__(self, initial: False):
        self.set(initial)
