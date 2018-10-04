import hdf5storage
import datetime
from datetime import date
import numpy as np

mat = hdf5storage.loadmat('wiki.mat')
wiki = mat['wiki']
gender = wiki['gender']
gender = gender[0,0]
photo_taken = wiki['photo_taken']
photo_taken = photo_taken[0,0]
dob = wiki['dob']
dob = dob[0,0]
path = wiki['full_path']
path = path[0,0]

def create_csv(file,name):
    a = pd.DataFrame(file)
    a.to_csv(name)
def datenum_to_datetime(datenum):
    """
    Convert Matlab datenum into Python datetime.
    :param datenum: Date in datenum format
    :return:        Datetime object corresponding to datenum.
    """
    days = datenum % 1
    hours = days % 1 * 24
    minutes = hours % 1 * 60
    seconds = minutes % 1 * 60
    return date.fromordinal(int(datenum)) \
           + timedelta(days=int(days)) \
           + timedelta(hours=int(hours)) \
           + timedelta(minutes=int(minutes)) \
           + timedelta(seconds=round(seconds)) \
           - timedelta(days=366)
#reshaping arrays rowwise

dob = np.reshape(dob,(62328,1))
gender = np.reshape(gender,(62328,1))
path = np.reshape(path,(62328,1))
photo_taken = np.reshape(photo_taken,(62328,1))
for i in range(len(dob)):
    a = datenum_to_datetime(int(dob[i,0]))
    dob[i,0] = a.year
for i in range(len(path)):
    a = str(path[i,0])
    a = list(a)
    a.pop()
    a.pop()
    del a[0]
    del a[0]
    a = ''.join(a)
    path[i,0] = a
create_csv(dob,name = 'dob.csv')
create_csv(gender,name = 'gender.csv')
create_csv(path,name = 'path.csv')
create_csv(photo_taken,name = 'photo_taken.csv')
