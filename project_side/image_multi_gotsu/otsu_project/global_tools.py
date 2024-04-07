import numpy as np

class Clean_data():     
    def clean_and_find_the_min_var(data, target):
        filtered_keys = filter(lambda x: target in data[x], data)
        min_key = min(filtered_keys, key=lambda x: data[x][target])
        min_var = data[min_key][target]
        return min_key, min_var
    
    def add_noise(dataset, object_numbers, noise_number, noise_type):
        if noise_type == "large":
            object_numbers = object_numbers * 0.5
        elif noise_type == "medium":
            object_numbers = object_numbers * 0.3
        elif noise_type == 'small':
            object_numbers = object_numbers * 0.1
            
        new_data = np.concatenate((dataset, np.full((len(dataset), object_numbers), noise_number)), axis=1)
        
        return new_data
    
    def add_single_photo_noise(dataset, add_numbers, noise_number, list_number, noise_type):
        if noise_type == 0:
            add_numbers = int(add_numbers * 0.75)
        elif noise_type == 1:
            add_numbers = int(add_numbers * 0.5)
        elif noise_type == 2:
            add_numbers = int(add_numbers * 0.25)        
        indices = np.where(dataset[list_number] == 128)[0][:add_numbers]
        dataset[list_number][indices] = noise_number
        return dataset

