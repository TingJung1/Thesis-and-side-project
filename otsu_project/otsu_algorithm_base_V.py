import numpy as np
from otsu_abc import Otsu
from calculation import Calculation
from read_images import Read_images

class Otsu_V(Otsu, Read_images):
    def __init__(self, dataset):
        Read_images.__init__(self)
        Otsu.__init__(self)
        self.dataset = dataset
      
    def otsu_variance(self, threshold):
        var = Calculation.variance(self.dataset, threshold, self.dataset.size)
        self.result[threshold].update({'otsu':var})
        return var

    def otsu_scanning_threshold(self, start, end):
        for th in range(start, end+1 ,1):
            self.otsu_variance(th)
    
    def calculation(self, threshold):
        index = self.dataset < threshold
        G1 = self.dataset[index]
        G2 = self.dataset[~index]
        G1_var = np.var(G1)
        G2_var = np.var(G2)
        self.result[threshold].update({'Cat1': G1_var})
        self.result[threshold].update({'Cat2': G2_var})
  
    def calculation_scanning_threshold(self, start, end):
        for th in range(start,end+1, 1 ):
            self.calculation(th)

    def result(self):
        return self.result
