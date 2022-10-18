import numpy as np


class Restriction:
    def __init__(self, pollutant):
        self.pollutant = pollutant

    def pm10(self) -> tuple:
        lim_inf = 0
        lim_sup = np.inf
        return lim_inf, lim_sup
