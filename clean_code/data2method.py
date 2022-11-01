import pandas as pd


def test_bootstrap(file_month, station) -> str:
    file_month_station = file_month[file_month.id_station_id == station]
    if file_month_station.id.count > 0:
        percent_null = file_month_station.original.isnull().sum()/file_month_station.id.count()
        if (percent_null >= 0.05) and (percent_null < 0.20):
            return "bootstrap"
        elif (percent_null >= 0.20) and (percent_null < 0.35):
            return "splines"
        elif (percent_null >= 0.35) and (percent_null < 0.5):
            return "duplicate_station"
        elif percent_null >= 0.5:
            return "nothing"
    return "distribution"


class data2method:

    def __init__(self, file, parameter):
        self.file = "/Users/phoebus/Documents/fileTesis/pollutants" + file + ".csv"
        self.parameter = parameter
        self.stations = ['PED', 'CAM', 'BJU', 'CCA', 'UAX', 'CUA', 'EDL', 'SFE', 'HGM',
                         'MCM', 'TEC', 'GAM', 'LAA', 'IZT', 'SAC', 'UAX', 'SNT', 'IBM',
                         'LOM', 'MGH', 'MPA', 'AJU', 'AJM', 'DIC', 'EAJ', 'MER', 'COR', 'TAH']

    def read_file(self) -> pd.DataFrame:
        print("[INFO] Se este leyendo el archivo "+self.file)
        df = pd.read_csv(self.file)
        df.dateUTCShiftedDown = pd.to_datetime(df.dateUTCShiftedDown)
        df = df[(df.dateUTCShiftedDown.dt.hour.between(6, 21)) &
                (df.id_station_id.isin(self.stations))&
                (df.id_parameter_id == self.parameter)]
        return df

    def extract_method(self) -> dict:
        stations_method = {}
        file = pd.read_csv(self.file)
        for month in range(1, 13):
            file_month = file[file.dt.month == month]
            stations_method[month] = {"bootstrap": [], "splines": [],
                                      "duplicate_station": [], "duplicate": [],
                                      "distribution": []}
            for station in self.stations:
                method = test_bootstrap(file_month=file_month, station=station)
                stations_method[month][method].append(station)
        return stations_method



