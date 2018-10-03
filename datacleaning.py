import pandas as pd
import gettingdata
path = pd.read_csv('path.csv')
dob = pd.read_csv('dob.csv')
gender = pd.read_csv('gender.csv')
photo = pd.read_csv('photo_taken.csv')
date = dob.iloc[:,1:2].values
photo_date = photo.iloc[:,1:2].values
path1 = path.iloc[:,1:2].values
gender1 = gender.iloc[:,1:2].values
#deleting dob below 1800
a = list()
for i in range(len(date)):
    if(date[i,0]<1800):
        a.append(i)
for i in range(len(a)):
    date = np.delete(date,a[i],0)
    path1 = np.delete(path1,a[i],0)
    photo_date = np.delete(photo_date,a[i],0)
    gender1 = np.delete(gender1,a[i],0)
    for j in range(i+1,len(a)):
        a[j] = a[j]-1 
#deleting nan from gender
b = np.isnan(gender1)
c = list()
for i in range(len(gender1)):
    if(b[i]==True):
        c.append(i)
for i in range(len(c)):
    date = np.delete(date,c[i],0)
    path1 = np.delete(path1,c[i],0)
    photo_date = np.delete(photo_date,c[i],0)
    gender1 = np.delete(gender1,c[i],0)
    for j in range(i+1,len(c)):
        c[j] = c[j]-1 
#getting age
age = np.ones((len(date),1))
for i in range(len(date)):
    age[i,0] = photo_date[i,0]-date[i,0]
#deleting age above 125 and below 2
a = list()
for i in range(len(date)):
    if(age[i,0]<0):
        a.append(i)
for i in range(len(a)):
    date = np.delete(date,a[i],0)
    path1 = np.delete(path1,a[i],0)
    photo_date = np.delete(photo_date,a[i],0)
    gender1 = np.delete(gender1,a[i],0)
    age = np.delete(age,a[i],0)
    for j in range(i+1,len(a)):
        a[j] = a[j]-1 
