import numpy as np
from gotsu_abc import GOtsu
from otsu_algorithm_base_G import Otsu_G
from calculation import Calculation
from scipy.optimize import differential_evolution

class GOTSU_G(GOtsu,Otsu_G):
    def __init__(self):
        Otsu_G.__init__(self,110)
        self.G_all={}

    def otsu_instance(self):
        for i in range(len(self.datasets)):
            self.G_all[i] = Otsu_G(self.datasets[i])

    def otsu_collection(self,threshold):  
        for v in self.G_all.values():  
            v.otsu_variance(threshold)
            v.calculation(threshold)      
              
    def otsu_collection_scanning(self, start, end):
        for th in range(start, end+1, 1):
            self.otsu_collection(th)

    def global_objective(self, threshold):
        self.otsu_collection(threshold)
        dataset_C1, dataset_C2, dataset_OT, ans = [], [], [], []
        for i, n in enumerate(self.G_all):
           dataset_C1.append(self.G_all[i].result[threshold]['Cat1'])
           dataset_C2.append(self.G_all[i].result[threshold]['Cat2'])
           dataset_OT.append(self.G_all[i].result[threshold]['otsu'])        
        for i, data in enumerate(zip(dataset_C1, dataset_C2)):
            ans.append(Calculation.global_calculation(data[0], data[1], dataset_C1, dataset_C2))
        ans, dataset_OT = np.array(ans), np.array(dataset_OT)
        result = ans + dataset_OT
        return result

    def global_objective_scanning(self, start, end):
        g = []
        for th in range(start, end+1, 1):
            g.append(self.global_objective(th))
        return g
    
    def global_objective_input_different_number(self, list):
        dataset_C1 = [self.G_all[i].result[list[i]]['Cat1'] for i in range(len(self.G_all))]
        dataset_C2 = [self.G_all[i].result[list[i]]['Cat2'] for i in range(len(self.G_all))]
        dataset_OT = [self.G_all[i].result[list[i]]['otsu'] for i in range(len(self.G_all))]        
        ans = [Calculation.global_calculation(dataset_C1[i], dataset_C2[i], dataset_C1, dataset_C2) for i in range(len(dataset_C1))]
        ans = np.array(ans)
        dataset_OT = np.array(dataset_OT)        
        result = ans + dataset_OT
        result = sum(result)
        return result
