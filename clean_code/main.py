# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# import bootstrap
# import joinfiles
import interpolation
## from simTreeLive import SimLiveTree
import matplotlib.pyplot as plt
import pandas as pd
# def print_hi(name):
#    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    # for year in range(2014, 2021):
    #     print(year)
    #     interpolacion = interpolation_tmp.InterpolationPollutant(file=path_files + str(year) + '.csv', parameter='PM10')
    #     file = interpolacion.inter_split()
    #     objeto = bootstrap.Bootstrap(file=path_files + str(year) + '.csv', parameter='PM10')
    #     file = objeto.bootstrap()
    # joinfiles.JoinFiles(file=file).sort_id_file()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    method2station = {1:{'interpolation':['CAM']}}
    df = pd.read_csv("/home/phoebus/Documents/code_tesis/files/pollutants2018.csv")
    df.dateUTCShiftedDown = pd.to_datetime(df.dateUTCShiftedDown)
    value = interpolation.Interpolation(station =method2station[1]["interpolation"][0] ,month = 1, 
                                        df = df[(df.dateUTCShiftedDown.dt.month == 1)&
                                                (df.id_station_id == method2station[1]["interpolation"][0])&
                                                (df.dateUTCShiftedDown.dt.hour.between(6,22))])
    value.filter_data()
    ## filter information return dict. Dict has month -> method -> station