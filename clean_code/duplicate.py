import numpy as np
import pandas as pd
from scipy.stats import pearsonr


def loop_values(values: np.ndarray, dup: float) -> np.ndarray:
    for value in values:
        if np.isnan(value):
            value = dup
    return values


class Duplicate_station:

    def __int__(self, df, station0, parameter="O3"):
        self.df = df
        self.station0 = station0
        self.stations = []
        self.parameter = parameter

    def test_correlation(self) -> list:
        stations_corr = []
        x_s = self.df[self.df.id_station_id == self.station0]
        for station in self.stations:
            y_s = self.df[self.df.id_station_id == station]
            test = pearsonr(x_s, y_s)
            if test[0] > 0.05:
                stations_corr.append(station)
        return stations_corr

    def ver_val(self, stations: list, date: str) -> float:
        df_sts = self.df[(self.df.id_station_id.isin(stations)) &
                         (self.df.dateUTCShiftedDown == date)]
        df_sts_no_nulls = df_sts[df_sts.original.notnull()]
        return df_sts_no_nulls.original.quantile(q=0.75)

    def dupl_value(self, date: str) -> pd.DataFrame:
        stations_corr = self.test_correlation()
        p75_station = self.ver_val(stations=stations_corr, date=date)
        df_station_clean = self.df[(self.df.id_station_id == self.station0) &
                                   (self.df.dateUTCShiftedDown == date)]
        clean_data = loop_values(df_station_clean.original, p75_station)
        df_station_clean.original = clean_data
        return df_station_clean
