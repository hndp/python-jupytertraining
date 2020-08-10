#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[277]:


x = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Des']
y = [1,2,3,4,5,6,7,8,9,10,11,12]
sales19 = [1,2,3,4,5,6,7,8,9,10,11,12]

y[0] = 1350039
y[1] = 5295835
y[2] = 3583583
y[3] = 8853284
y[4] = 7385243
y[5] = 8247357
y[6] = 2384583
y[7] = 6863358
y[8] = 10274375
y[9] = 7357281
y[10] = 8321853
y[11] = 9274863

sales19[0] = ('$1.350.039')
sales19[1] = ('$5.295.835')
sales19[2] = ('$3.583.583')
sales19[3] = ('$8.853.284')
sales19[4] = ('$7.385.243')
sales19[5] = ('$8.247.357')
sales19[6] = ('$2.384.583')
sales19[7] = ('$6.863.358')
sales19[8] = ('$10.274.375')
sales19[9] = ('$7.357.281')
sales19[10] = ('$8.321.853')
sales19[11] = ('$9.274.863')

plt.plot(x, y, label = '2019', marker = '.', markeredgecolor = 'black', markersize = '15')
plt.title('hndp industry', {'fontsize': 20})
plt.ticklabel_format(style='plain', axis='y')
plt.text(x[0],y[0],sales19[0])
plt.text(x[1],y[1],sales19[1])
plt.text(x[2],y[2],sales19[2])
plt.text(x[3],y[3],sales19[3])
plt.text(x[4],y[4],sales19[4])
plt.text(x[5],y[5],sales19[5])
plt.text(x[6],y[6],sales19[6])
plt.text(x[7],y[7],sales19[7])
plt.text(x[8],y[8],sales19[8])
plt.text(x[9],y[9],sales19[9])
plt.text(x[10],y[10],sales19[10])
plt.text(x[11],y[11],sales19[11])
plt.legend()
plt.show()


x1 = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Des']
y1 = [1,2,3,4,5,6,7,8,9,10,11,12]
sales20 = [1,2,3,4,5,6,7,8,9,10,11,12]

y1[0] = 3520439
y1[1] = 4235835
y1[2] = 7583583
y1[3] = 8863484
y1[4] = 5685543
y1[5] = 2347657
y1[6] = 3784283
y1[7] = 4663558
y1[8] = 6674575
y1[9] = 7757781
y1[10] = 9731553
y1[11] = 7874463

sales20[0] = ('$3.520.439')
sales20[1] = ('$4.235.835')
sales20[2] = ('$7.583.583')
sales20[3] = ('$8.863.484')
sales20[4] = ('$5.685.543')
sales20[5] = ('$2.347.657')
sales20[6] = ('$3.784.283')
sales20[7] = ('$4.663.558')
sales20[8] = ('$6.674.575')
sales20[9] = ('$7.757.781')
sales20[10] = ('$9.731.553')
sales20[11] = ('$7.874.463')

plt.plot(x1, y1, label = '2020', marker = '.', markeredgecolor = 'black', markersize = '15')
plt.title('hndp industry', {'fontsize': 20})
plt.ticklabel_format(style='plain', axis='y')
plt.text(x1[0],y1[0],sales20[0])
plt.text(x1[1],y1[1],sales20[1])
plt.text(x1[2],y1[2],sales20[2])
plt.text(x1[3],y1[3],sales20[3])
plt.text(x1[4],y1[4],sales20[4])
plt.text(x1[5],y1[5],sales20[5])
plt.text(x1[6],y1[6],sales20[6])
plt.text(x1[7],y1[7],sales20[7])
plt.text(x1[8],y1[8],sales20[8])
plt.text(x1[9],y1[9],sales20[9])
plt.text(x1[10],y1[10],sales20[10])
plt.text(x1[11],y1[11],sales20[11])
plt.legend()
plt.show()

plt.plot(x, y, label = '2019', marker = '.', markeredgecolor = 'black', markersize = '15')
plt.plot(x1, y1, label = '2020', marker = '.', markeredgecolor = 'black', markersize = '15')
plt.title('hndp industry', {'fontsize': 20})
plt.ticklabel_format(style='plain', axis='y')
plt.legend()
plt.show()

print("2020 sales compared to 2019 sales :")
print("")

print(x[0], "=", "$", y1[0] - y[0])
print(x[1], "=", "$", y1[1] - y[1])
print(x[2], "=", "$", y1[2] - y[2])
print(x[3], "=", "$", y1[3] - y[3])
print(x[4], "=", "$", y1[4] - y[4])
print(x[5], "=", "$", y1[5] - y[5])
print(x[6], "=", "$", y1[6] - y[6])
print(x[7], "=", "$", y1[7] - y[7])
print(x[8], "=", "$", y1[8] - y[8])
print(x[9], "=", "$", y1[9] - y[9])
print(x[10], "=", "$", y1[10] - y[10])
print(x[11], "=", "$", y1[11] - y[11])
print("")

print("Total =", sum(y1) - sum(y))


# In[ ]:




