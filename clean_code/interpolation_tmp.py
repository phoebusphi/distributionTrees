import numpy as np
import pandas as pd
 
from sortFilter import FilterData
"""
En esta sección realizaremos la interpolacion de 
algunos elementos para poder rellenar los datos.

1. Tomando el archivo que se genero con el metodo de 
boostrap.
2. Seleccionaremos las estaciones que cumplan los requerimientos.
3. Se generara una función para aproximar el los puntos.
Se filtra por estación de monitoreo y se toman todos los puntos dado esa estación.

Se usara la interpolación cuando la cantidad de valores nulos en una estación de monitoreo 
tenga el 20 horas de valores no encontrados
"""


class InterpolationPollutant:
    def __init__(self, file, parameter):
        self.file = file
        self.parameter = parameter
        self.hours = 30
        self.stations = ['PED', 'CAM', 'BJU', 'CCA', 'UAX', 'CUA', 'EDL', 'SFE', 'HGM',
                         'MCM', 'TEC', 'GAM', 'LAA', 'IZT', 'SAC', 'UAX', 'SNT', 'IBM',
                         'LOM', 'MGH', 'MPA', 'AJU', 'AJM', 'DIC', 'EAJ', 'MER', 'COR', 'TAH']
        self.values = np.array([])

    def fx(self) -> dict:
        functions = {'PM10': [], 'O3': [],
                     'TMP': [], 'RH': []}
        return functions

    def interpolate_value(self, df, station) -> np.ndarray:
        df_station = df[(df.id_station_id == station) &
                        (df.id_parameter_id == self.parameter)]
        xs = df_station[(df_station.original.notna())].dateUTCShiftedDown
        x_original = np.arange(0, xs.dateUTCShiftedDown.size, 1)
        y_original = xs.original.values
        tck = interpolate.splrep(x_original, y_original, s=0)
        x_inter_original = np.arange(0, df_station.dateUTCShiftedDown.size, 1)
        y_inter_original = interpolate.splev(x_inter_original, tck)
        x_null = df_station.original.values
        for i in range(df_station.dateUTCShiftedDown.size):
            if np.isnan(x_null[i]) and not(np.isnan(y_inter_original[i])):
                x_null = y_inter_original[i]
        return x_null

    def inter_split(self):
        fdata = FilterData(file=self.file, hour2day=30, parameter="PM10")
        data = fdata.read_file()
        month = 1
        station_inter_fill = fdata.rank_stations(data=data, month=month).id_station_id.values
        for station in station_inter_fill:
            self.values = self.interpolate_value(df=data, station=station)
        return self.values












