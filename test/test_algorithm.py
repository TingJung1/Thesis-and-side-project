from otsu_project.calculation import Calculation
import numpy as np
from otsu_project.global_tools import Clean_data
def test_variance():
    g1 = np.array([1,2,2,2,5,5,6,6])
    g2 = np.array([8,12,12,12,15,15,16,16])
    pixel_number = 16
    object = Calculation.between_variance(g1,g2,pixel_number)
    assert round(object,4) == 5.2109

def test_cut_twice_and_calculate_mean():
    dataset = [2,2,2,4,5,5,6]
    dataset = np.array(dataset, dtype = 'int64')
    t=3
    object = Calculation.cut_twice_and_calculate_mean(dataset,t)
    assert object['g1'] == 2 and  object['g2'] == 5

def test_g_global_calculation():
    g1 = [1,2,3,4,5]
    g2 = [3,4,5,6,7]
    object = Calculation.g_global_calculation(g1[0], g2[0], g1, g2)
    assert object == 8

def test_add_noise():    
    # Save a copy of the original dataset
    a = np.full((100,), 128)
    b = np.full((100,), 122)
    c = np.full((100,), 126)
    result = np.vstack([a, b, c])
    # Add noise to the first list
    dataset_with_noise = Clean_data.add_single_photo_noise(result, 50, 130, 0, 0)
    # Check that only the first 50 128's have been changed to 130
    assert np.all(dataset_with_noise[0][:25] == 130)
    assert np.all(dataset_with_noise[0][75:] == 128)
    # Check that the other two lists are unchanged
    assert np.all(dataset_with_noise[1] == result[1])
    assert np.all(dataset_with_noise[2] == result[2])