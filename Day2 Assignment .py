#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from numpy.random import randn, randint, uniform, sample


# In[4]:


df = pd.DataFrame(randn(10, 4), columns=['a', 'b', 'c', 'd'])
df


# In[6]:


df.plot.bar(figsize = (10,10))
plt.title('Graph Day2')


# In[ ]:




