import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.model_selection import train_test_split


class DBSCAN_Dead:

    def __int__(self, data, stations, train=0.8, seed=10):
        self.data = data
        self.train = train
        self.seed = seed
        self.stations = list(stations)
        self.parameters = ["PM10", "O3"]

    def __filter_info__(self) -> pd.DataFrame:
        self.data.dateUTCShiftedDown = pd.to_datetime(self.data.dateUTCShiftedDown)
        self.data = self.data[(self.data.id_parameter_id.isin(self.parameters)) &
                              (self.data.id_station_id.isin(self.stations)) &
                              (self.data.original.notnull())]
        return self.data

    def __add_info__(self) -> np.array:
        df_pm10 = self.data[self.data.id_parameter_id == "PM10"]
        df_o3 = self.data[self.data.id_parameter_id == "O3"]
        water = np.random.normal(100, 10, 2000)
        pm10 = []
        o3 = []
        for i in range(0, 3000, 10):
            pm10.append(np.percentile(df_pm10.original.iloc[i:10 + i], 75))
            o3.append(np.percentile(df_o3.original.iloc[i:10 + i], 75))
        dat = np.ones([2000, 3])
        dat[:, 0] = pm10
        dat[:, 1] = o3
        dat[:, 2] = water
        return dat

    def model_dbscan(self, plot=True) -> None:
        dat = self.__add_info__()
        clustering = DBSCAN(eps=13, min_samples=30).fit(dat)
        labels = clustering.labels_
        filename = 'dbscan_pm10_model.sav'
        pickle.dump(clustering, open(filename, 'wb'))
        load_dbscan_model = pickle.load(open(filename, 'rb'))
        if plot:
            ax = plt.axes(projection='3d')
            ax.scatter(dat[:, 0], dat[:, 1], dat[:, 2], c=labels)
            ax.set_xlabel("pm10")
            ax.set_ylabel("o3")
            ax.set_zlabel("water")
            plt.show()
        else:
            print(np.unique(labels))
