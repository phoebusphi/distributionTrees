## En este archivo se ordenara y se filtrara las estaciones
##
##

import pandas as pd


class FilterData:
    def __init__(self, file, hour2day, parameter):
        self.file = "/Users/phoebus/Documents/fileTesis/pollutants"+file+".csv"
        self.hour2day = hour2day
        self.parameter = parameter
        self.stations = ['PED', 'CAM', 'BJU', 'CCA', 'UAX', 'CUA', 'EDL', 'SFE', 'HGM',
                         'MCM', 'TEC', 'GAM', 'LAA', 'IZT', 'SAC', 'UAX', 'SNT', 'IBM',
                         'LOM', 'MGH', 'MPA', 'AJU', 'AJM', 'DIC', 'EAJ', 'MER', 'COR', 'TAH']

    def read_file(self) -> pd.DataFrame:
        df = pd.read_csv(self.file)
        df.dateUTCShiftedDown = pd.to_datetime(df.dateUTCShiftedDown)
        df = df[(df.dateUTCShiftedDown.dt.hour.between(6, 21)) &
                (df.id_station_id.isin(self.stations))]
        return df

    def rank_stations(self, data, month) -> pd.DataFrame:
        df_f = data[(data.dateUTCShiftedDown.dt.month == month) &
                    (data.id_station_id.isin(self.stations)) &
                    (data.dateUTCShiftedDown.dt.hour.between(6, 21)) &
                    (data.id_parameter_id == self.parameter) &
                    (data.original.isna())]
        rank_nulls = df_f[['id_station_id', 'id']].groupby('id_station_id').size()\
            .sort_values(ascending=True).reset_index(name='nulls')
        rank_nulls = rank_nulls[rank_nulls.nulls <= self.hour2day]
        return rank_nulls