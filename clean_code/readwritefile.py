# En este archivo se generaran los csv con los datos de los arboles de cuando fueron plantados
# y tambien se moveran lo que ya se murieron
#

import pandas as pd
import os


def create_file() -> pd.DataFrame:
    df = {'id': [],
          'date': [],
          'tree': [],
          'plant': [],
          'zone': [],
          'days_live': [],
          'li_de': []
          }
    df = pd.DataFrame(df)
    return df


class GenerateFile:
    def __int__(self):
        self.path = "path"
        self.history_file = "trees_history.csv"
        self.dead_file = "trees_dead.csv"
        self.df = None

    def insert_row(self, **data) -> pd.DataFrame:
        data['li_de'] = 1
        self.df.loc[len(self.df.index)] = data.values()
        return self.df

    def alter_row(self, *indexes) -> pd.DataFrame:
        self.df = self.df.replace({'li_de': list(self.df[self.df.id.isin(indexes)].to_dict()['li_de'].values())}, -1)
        return self.df

    def main(self) -> None:
        if os.path.exists("./"+self.history_file):
            self.df = self.insert_row()
            self.df = self.alter_row()
        else:
            self.df = create_file()
        self.df.to_csv(self.history_file)
