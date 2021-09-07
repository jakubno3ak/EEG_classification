from typing import *
import pandas as pd
import numpy as np
import os


class CustomRBReader(object):
    __FREQUENCY = 256

    def __init__(self, read_path=None):
        if not isinstance(read_path, str):
            raise TypeError
        else:
            self._read_path = read_path
        self._time_axis = np.linspace(0, 1, self.__FREQUENCY, endpoint=False)
        self.data = None

    @property
    def read_path(self) -> str:
        return self._read_path

    @read_path.setter
    def read_path(self, new_path):
        if not isinstance(new_path, str):
            raise TypeError
        else:
            self._read_path = new_path

    @property
    def time_axis(self) -> np.ndarray:
        return self._time_axis

    def open_file(self):
        with open(self.read_path) as file:
            lines = file.readlines()
            file.close()
        lines = list(map(lambda line: str(line).strip("b'# ").split(), lines))
        self.data = [lines[0], lines[4:]]  # only name of subject and data without dataset description

    def get_channels(self) -> list:
        columns = ['time']
        channels = [channel[1] for channel in self.data[1][0::257]]
        columns.extend(channels)
        return columns

    def prepare_df(self) -> dict:
        del self.data[1][0::257]
        res = [float(sample[3].strip('\\n')) for sample in self.data[1]]
        res = np.array(res).reshape(64, 256).transpose()
        res = np.concatenate((self.time_axis.reshape(-1, 1), res), axis=1)
        #df = pd.DataFrame(res, columns=self.get_channels())
        return {'subject': self.data[0][0],
                'data': res,
                'label': self.data[0][0][3]}
