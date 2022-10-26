import numpy as np
import pandas as pd

class Interpolation:
    def __init__(self,station,month,df,parameter="O3") -> None:
        self.df = df
        self.station = station
        self.month = month
        self.parameter = parameter
    
    def filter_data(self) -> None:
        df = self.df[(self.df.id_parameter_id == self.parameter)]
        print(df.id.count())
        x_original = np.arange(0, df.dateUTCShiftedDown.size, 1)
        y_original = df.original.values
        tck = interpolate.splrep(x_original, y_original, s=0)
        x_inter_original = np.arange(0, df_station.dateUTCShiftedDown.size, 1)
        y_inter_original = interpolate.splev(x_inter_original, tck)
        x_null = df_station.original.values
        for i in range(df_station.dateUTCShiftedDown.size):
            if np.isnan(x_null[i]) and not(np.isnan(y_inter_original[i])):
                x_null = y_inter_original[i]
        return x_null