from itertools import product
from gotsu_algorithm_G import GOTSU_G
from global_tools import Clean_data
import random
import math
import numpy as np 
from gotsu_algorithm_V import GOTSU_V
from gotsu_algorithm_GV import GOTSU_GV
from gotsu_algorithm_GV_weight import GOTSU_GV_w
import multiprocessing as mp
import logging
from datetime import datetime
import os
import pickle


class heristic_algorithm(): 
    def find_the_minimum(my_dict, parameter):
        my_dict = {k: v for k, v in my_dict.items() if v and not np.isnan(v[parameter]) and v[parameter]!=0}
        if not my_dict:
            return None, None
        min_key = min(my_dict, key=lambda k: my_dict[k][parameter] if not np.isnan(my_dict[k][parameter]) and my_dict[k][parameter]!=0 else float('inf'))
        min_value = my_dict[min_key][parameter]
        return min_key, min_value              
    def find_the_cat1(my_dict, parameter,cat1):
        my_dict = {k: v for k, v in my_dict.items() if v and not np.isnan(v[parameter]) and v[parameter]!=0}
        if not my_dict:
            return None, None
        min_key = min(my_dict, key=lambda k: my_dict[k][parameter] if not np.isnan(my_dict[k][parameter]) and my_dict[k][parameter]!=0 else float('inf'))
        min_value = my_dict[min_key][cat1]
        return min_key, min_value  
         
    def heuristic_search(method, list, threshold, j):
        start = threshold -3
        better_value = method.global_objective_input_different_number(list)
        min_threshold = list[j]
        for i in range(6):
            start += 1
            list[j] = start
            objective_value = method.global_objective_input_different_number(list)
            if objective_value < better_value:
                better_value = objective_value
                min_threshold = list[j]
        print (min_threshold)
        return min_threshold
         
    def store_the_otsu_information(dataset, G_all):
        otsu_info_list = []
        for i, n in enumerate(dataset):
            min_threshold, min_otsu = heristic_algorithm.find_the_minimum(G_all[i].result, 'otsu')
            if not math.isnan(min_otsu) and min_otsu != 0:
                otsu_info_list.append(min_threshold)
                print(f"Photo {i}: Otsu minimum at threshold {min_threshold}: {min_otsu}")
            else:
                print(f"Photo {i}: No valid Otsu minimum found")
        return otsu_info_list
    
    def heristic_model_otsu_random_start(method,dataset,otsu_list):
        prev_otsu_list = otsu_list.copy()
        for k in range(200):
            print(f'第{k}個iteration')
            j_list = random.sample(range(len(dataset)), len(dataset))
            for j in range(len(dataset)):                
                threshold = otsu_list[j_list[j]]
                otsu_list[j_list[j]] = heristic_algorithm.heuristic_search(method,otsu_list,threshold,j_list[j])
            # 檢查是否達到停止條件
            if otsu_list == prev_otsu_list:
                print(f"第{k}:iteration")
                break
            else:
                prev_otsu_list = otsu_list.copy()
        return otsu_list
