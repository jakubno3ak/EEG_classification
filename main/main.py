from utils.CustomRBReader import CustomRBReader
from utils.CustomPlotter import CustomPlotter

PATH = r"D:\program_files_d\python\master\dataset\alco\co2a0000365\co2a0000365.rd.004"

if __name__ == "__main__":
    reader = CustomRBReader(PATH)
    reader.open_file()
    data = reader.prepare_df()
    plotter = CustomPlotter(data)
    channel = reader.get_channels()[10]
    plotter.plot_single_sensor(channel)
    print(data)
    #  plotter.plot_all_sensors()
