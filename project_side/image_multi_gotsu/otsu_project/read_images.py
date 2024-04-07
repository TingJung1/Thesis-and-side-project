import cv2
from plantcv import plantcv as pcv
import numpy as np
import matplotlib as plt
import os
from PIL import Image


class Read_images():
    def __init__(self):
        self.to_show_photos = []
        self.dataset = [] 
        self.datasets = []
        
    def read_image(self, pathway):
        try:
            with Image.open(pathway) as img:
                img = cv2.imread(pathway)
                gray_img = pcv.rgb2gray_lab(rgb_img=img, channel = 'a')    
            print(f"The file '{pathway}' exists and can be opened.")
        except OSError:
            print(f"The file '{pathway}' is not a valid image file.")
        self.to_show_photos.append(gray_img)
        gray_img_concatenate = np.concatenate(gray_img)
        dataset = np.array(gray_img_concatenate, dtype = 'int64')
        self.dataset = dataset
        return gray_img_concatenate
    
    def read_folder(self, pathway):
        
        for filename in os.listdir(pathway):
            if filename.endswith(".png") or filename.endswith(".jpg"):
                img_path = os.path.join(pathway, filename)
                dataset = self.read_image(img_path)
                self.datasets.append(dataset)
        self.datasets = np.array(self.datasets)
                
        
  
class Visulation(Read_images):   
    def histogram_visualization(self):
        img = self.dataset
        hist = cv2.calcHist([img],[0],None,[256],[0,256])
        hist1 = hist.flatten()
        plt.bar(range(0,256), hist1)
        plt.show()
        return hist, hist1
    def segement_threshold(self,threshold):
        ret1, th2 = cv2.threshold(self.dataset, threshold, 255, cv2.THRESH_BINARY)
        plt.imshow(th2)
        plt.title(threshold)
        plt.show()



