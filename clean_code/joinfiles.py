import pandas as pd
import datetime as dt
import numpy as np
"""
En este archivo se unira la información con los valores que se rellenaron 
identificandolos por medio de la fecha
Lo que se hara es lo siguiente:

date|parameter|station|value
xxx |pm1      |st1    |none
xyx |pm2      |st1    |123    -> 
xxy |pm1      |st1    |none
"""


class JoinFiles:
    def __init__(self, file):
        self.df_original = pd.read_csv(file)
        self.df_split = pd.read_csv("split" + file)
        self.df_boot = pd.read_csv("boot" + file)
        self.df_final = {'id': [], 'dateUTCShiftedDown': [], 'date': [],
                         'original': [], 'fixed': [], 'UTC_hour_id': [],
                         'id_parameter_id': [], 'id_station_id': []}

    def sort_id_file(self):
        id_original = self.df_original.id.values
        id_split = self.df_split.id.values
        id_boot = self.df_boot.id.values
        len_max = np.max(id_original.size, id_split.size, id_boot.size)
        tmp = []
        for row in range(len_max):
            if row < id_original.size:
                tmp.append(id_original[row])
            if row < id_split.size:
                tmp.append(id_split[row])
            if row < id_boot.size:
                tmp.append(id_boot[row])
            tmp = sorted(tmp)
            self.df_final['id'].extend(tmp)
            for sort_ids in tmp:
                if self.df_original[self.df_original.id == sort_ids].id.count() > 0:
                    self.fill_row(self.df_original[self.df_original.id == sort_ids])
                if self.df_split[self.df_split.id == sort_ids].id.count() > 0:
                    self.fill_row(self.df_split[self.df_split.id == sort_ids])
                if self.df_boot[self.df_boot.id == sort_ids].id.count() > 0:
                    self.fill_row(self.df_boot[self.df_boot.id == sort_ids])

    def fill_row(self, df):
        for key in self.df_final:
            self.df_final[key].append(df[key].iloc[0])







