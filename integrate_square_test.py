#!/usr/bin/env python
# coding: utf-8

# In[21]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


# In[22]:


energy_coords = np.linspace(0,.1,30)
#print(energy_coords)
time_coords = np.linspace(0,5,100)
#print(time_coords)

fluence, fluence1 = np.meshgrid(time_coords, energy_coords)


# In[90]:


fig, (ax1) = plt.subplots(1, 1, figsize=(22, 5))
pcm1 = ax1.pcolormesh(time_coords, energy_coords, fluence1)
#plt.show()
# Coordinates of rectangle vertices
# in clockwise order
xs = [1, 2, 2, 1, 1]
ys = [0.04, 0.04, 0.06, 0.06, 0.04]
ax1.plot(xs, ys, color="white")

plt.show()


# In[89]:


# add elements inside edges of rectangle

integrated_box = 0
for i, time in enumerate(time_coords):
    if time > 1 and time < 2:
        for j, energy in enumerate(energy_coords):
            if energy > 0.04 and energy < 0.06:
                #print(i,time,j,energy)
                integrated_box += fluence1[j][i]
            
print(integrated_box)


# In[ ]:




