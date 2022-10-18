# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import bootstrap
import interpolation
import joinfiles
from simTreeLive import SimLiveTree
import matplotlib.pyplot as plt
# def print_hi(name):
#    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def fill_data(path_files):
    for year in range(2014, 2021):
        print(year)
        interpolacion = interpolation.InterpolationPollutant(file=path_files + str(year) + '.csv', parameter='PM10')
        file = interpolacion.inter_split()
        objeto = bootstrap.Bootstrap(file=path_files + str(year) + '.csv', parameter='PM10')
        file = objeto.bootstrap()
    joinfiles.JoinFiles(file=file).sort_id_file()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # l = []
    # for i in range(100):
    #     v = 0
    #     for j in range(10):
    #         v += SimLiveTree(50, 1000).simulation()
    #     l.append(v/10)
    #     print(i)

    valor = SimLiveTree(-60, 1000).simulation()
    plt.plot(valor[0], valor[1])
    plt.show()