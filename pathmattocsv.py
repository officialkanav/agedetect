import pandas as pd
import numpy as np

import scipy.io
mat = scipy.io.loadmat('path1.mat')
a = mat['a']
path = list()
for i in range(0,62328):

    t = str(a[0,i])
    path.append(t)

for i in range(0,62328):
    a = list(path[i])
    a.pop()
    a.pop()
    del a[0]
    del a[0]
    a = ''.join(a)
    path[i] = a
path = pd.DataFrame(path)
path.to_csv('path.csv')
