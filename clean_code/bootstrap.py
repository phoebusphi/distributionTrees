import numpy as np
import pandas as pd
from sortFilter import FilterData
import seaborn as sns


"""
Tomaremos los datos de un parametro con una cierta 
distribución y los normalizaremos de esta manera 
podemos rellenar los datos de faltantes.
Pseudocodigo
1.- Rank de las estaciones con valores nulos.
1.- Se toman a las estaciones de monitoreo con menor 
    cantidad de valores nulos en un mes.
2.- Se toma a la estación i-ésima y se separa la información 
    por conjuntos
3.- A cada conjunto se le saca el promedio, se obtiene 
    el promedio global junto con la desviación y su varianza. 
"""


class Bootstrap:
    def __init__(self, file, parameter, group=5):
        self.file = file
        self.group = group
        self.stations = ['PED', 'CAM', 'BJU', 'CCA', 'UAX', 'CUA', 'EDL', 'SFE', 'HGM',
                         'MCM', 'TEC', 'GAM', 'LAA', 'IZT', 'SAC', 'UAX', 'SNT', 'IBM',
                         'LOM', 'MGH', 'MPA', 'AJU', 'AJM', 'DIC', 'EAJ', 'MER', 'COR', 'TAH']
        self.parameter = parameter
        self.days2hrs = 30

    # def read_file(self) -> pd.DataFrame:
    #     df = pd.read_csv(self.file)
    #     df.dateUTCShiftedDown = pd.to_datetime(df.dateUTCShiftedDown)
    #     df = df[(df.dateUTCShiftedDown.dt.hour.between(6, 21)) &
    #             (df.id_station_id.isin(self.stations))]
    #     return df
    #
    # def rank_stations(self, data, month) -> pd.DataFrame:
    #     df_f = data[(data.dateUTCShiftedDown.dt.month == month) &
    #                 (data.id_station_id.isin(self.stations)) &
    #                 (data.dateUTCShiftedDown.dt.hour.between(6, 21)) &
    #                 (data.id_parameter_id == self.parameter) &
    #                 (data.original.isna())]
    #     rank_nulls = df_f[['id_station_id', 'id']].groupby('id_station_id').size()\
    #         .sort_values(ascending=True).reset_index(name='nulls')
    #     rank_nulls = rank_nulls[rank_nulls.nulls <= self.days2hrs]
    #     return rank_nulls

    def mean_data(self, df, stations_f, month) -> dict:
        df_f = df[(df.dateUTCShiftedDown.dt.month == month) &
                  (df.id_station_id.isin(stations_f)) &
                  (df.dateUTCShiftedDown.dt.hour.between(6, 21)) &
                  (df.id_parameter_id == self.parameter) &
                  (df.original.notnull())]
        df_val = df_f.original.values
        r = df_val.size % self.group
        large = (df_val.size - r)//self.group
        b = np.zeros((self.group, large))
        for i in range(self.group):
            index_random = np.random.randint(0, df_val.size, large)
            b[i, :] = df_val[index_random]
            df_val = np.delete(df_val, index_random)
        mean_rows = np.mean(b, axis=1)
        mean_stations = {station: mean_rows[i] for station, i in zip(stations_f, range(mean_rows.size))}
        return mean_stations

    def fill_df(self, df, mean_st, month) -> pd.DataFrame:
        if len(mean_st) > 0:
            rows = []
            for station in mean_st:
                val_id = df[(df.id_station_id == station) &
                            (df.dateUTCShiftedDown.dt.month == month) &
                            (df.original.isna()) &
                            (df.id_parameter_id == self.parameter)].index
                rows.extend(val_id.values)
            for row in rows:
                values = df.loc[row]
                df.at[row, 'original'] = mean_st[values['id_station_id']]
        return df

    def bootstrap(self):
        fdata = FilterData(file=self.file, hour2day=50, parameter="PM10")
        data = fdata.read_file()
        for month in range(1, 13):
            print('mes ', month)
            station_fill = fdata.rank_stations(data=data, month=month).id_station_id
            mean_df = self.mean_data(data, station_fill, month)
            df_fill = self.fill_df(data, mean_df, month)
            data = df_fill
        df_boot = pd.DataFrame(data)
        df_boot.to_csv(self.file[:45]+'_boot_'+self.file[45:], index=False)

