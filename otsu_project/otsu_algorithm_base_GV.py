from otsu_abc import Otsu
from calculation import Calculation
from read_images import Read_images
import numpy as np
class Otsu_GV(Otsu, Read_images):
    def __init__(self,dataset):
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
        g1_g2 = Calculation.cut_twice_and_calculate_mean(self.dataset, threshold)
        g1_mean = g1_g2['g1']
        g2_mean = g1_g2['g2']
        self.result[threshold].update({'Cat1' : g1_mean})
        self.result[threshold].update({'Cat2' : g2_mean})
        index = self.dataset < threshold
        G1 = self.dataset[index]
        G2 = self.dataset[~index]
        G1_var = np.var(G1)
        G2_var = np.var(G2)
        self.result[threshold].update({'Cat3': G1_var})
        self.result[threshold].update({'Cat4': G2_var})
    
    def calculation_scanning_threshold(self, start, end):
        for th in range(start, end+1, 1 ):
            self.calculation(th)

    def result(self):
        return self.result