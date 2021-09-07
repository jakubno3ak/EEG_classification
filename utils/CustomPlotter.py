import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
import pandas as pd


class CustomPlotter(object):
    __FREQUENCY = 256

    def __init__(self, data):
        if not isinstance(data, dict):
            raise TypeError
        else:
            self._data = data

    @property
    def data(self) -> dict:
        return self._data

    @data.setter
    def data(self, new_data):
        if not isinstance(new_data, dict):
            raise TypeError
        else:
            self._data = new_data

    def plot_single_sensor(self, sensor_label: str):
        plt.plot(self.data['data_frame'].index, self.data['data_frame'][sensor_label])
        plt.grid()
        plt.title(f"EEG {sensor_label}, SUBJECT {self.data['subject']}")
        plt.xlabel(f"TIME [sec] with freq {self.__FREQUENCY}")
        plt.ylabel(f"Voltage [mV]")
        plt.show()

    def plot_all_sensors(self):
        time_axis = self.data['data_frame'].index
        sensor_idx_axis = [x for x in range(len(self.data['data_frame'].iloc[0]))]
        time_axis, sensor_idx_axis = np.meshgrid(time_axis, sensor_idx_axis)
        voltage_grid = np.zeros_like(time_axis)
        for i in range(time_axis.shape[1]):
            for j in range(time_axis.shape[0]):
                voltage_grid[j][i] = self.data['data'][i][j]

        ax = plt.axes(projection='3d')
        ax.contour3D(sensor_idx_axis, time_axis, voltage_grid, 100, cmap='coolwarm')
        plt.show()
