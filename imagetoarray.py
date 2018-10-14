!pip install tqdm
import pandas as pd
import numpy as np
import os
from tqdm import tqdm
import cv2
from sklearn.preprocessing import OneHotEncoder
class images_to_array():
    def __init__(self,imagesize,directory,agedirec):
        self.imagesize = imagesize
        self.directory = directory
        self.agedirectory = agedirec
    def extract(self):
        a = os.listdir(self.directory)
        labels = pd.read_csv(self.agedirectory)
        age = labels.iloc[:,1:2].values

        ohe = OneHotEncoder(categorical_features = [0])
        age = ohe.fit_transform(age).toarray()
        d = 3*self.imagesize
        image = np.ones((23708,d,self.imagesize),int)
        image = np.reshape(image,(23708,self.imagesize,self.imagesize,3))
        for i in tqdm(range(len(a))):
          path = os.path.join(self.directory,str(a[i]))
          image1 = cv2.imread(path)
          image1 = cv2.resize(image1,(self.imagesize,self.imagesize))
          image[i,:,:,:] = image1