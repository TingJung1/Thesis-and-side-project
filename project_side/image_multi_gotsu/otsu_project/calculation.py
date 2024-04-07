import numpy as np


class Calculation():

    @staticmethod
    def between_variance(g1,g2,total_pixel):
        try:        
            a = (len(g1)/total_pixel) * np.var(g1) + (len(g2)/total_pixel) * np.var(g2)
            return a
        except ZeroDivisionError:
            print("Cannot divide by zero!")
            return None

            
    def variance(dataset,threshold,total_pixel):
        index = dataset < threshold
        g1 = dataset[index]
        g2 = dataset[~index]
        var = Calculation.between_variance(g1,g2,total_pixel)
        return var

    @staticmethod
    def cut_twice_and_calculate_mean(dataset,threshold):
        index = dataset < threshold
        g1 = np.mean(dataset[index])
        g2 = np.mean(dataset[~index])
        return {'g1': g1, 'g2' : g2}

    @staticmethod
    def global_calculation(g1, g2, group1, group2):
        ans = (g1- np.mean(group1)) **2 + (g2-np.mean(group2)) **2
        return ans 