import numpy as np
import pandas as pd
from scipy.interpolate import CubicSpline

class Interpolation:
    def __init__(self, df, parameter="O3") -> None:
        self.df = df[df.id_parameter_id==parameter]
    
    def find_index_null(self,data_original) -> set:
        index = np.where(np.isnan(data_original.values))
        index_null = set(); index_null.add(index[0])
        for i in range(len(index)-1):
            if index[i] + 1 != index[i+1]:
                index_null.add(index[i])
        return index_null

    def fill_data(self, index, data_original) -> pd.DataFrame:
        x = data_original.id.size
        y = data_original.original[data_original.original.notnull()].values
        xs = CubicSpline(x, y)
        for i in range(len(index)-1):
            a, b = index[0], index[1]
            diff = b - a
            x_p = np.linspace(np.pi/3, 2*np.pi,diff)
            sus_d = xs(x_p); k = 0
            for j in range(a, b):
                data_original.original.iloc[j] = sus_d[k]
                k+=1
        return data_original
    
    def spline_fill(self) -> pd.DataFrame:
        index_nulls = self.find_index_null(self.df.original)
        data_f = self.fill_data(index=index_nulls, data_original=self.df)
        return data_f