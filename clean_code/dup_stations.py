import numpy as np
import pandas as pd

neighbours = {}

class Duplicate:
    
    def __init__(self, df, station) -> None:
        self.df = df
        self.station = station
    
    def find_neighbour(self):
        pass