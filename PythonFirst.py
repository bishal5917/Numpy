#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


array=np.array([[2,4,5,8]],np.int64)


# In[3]:


array[0,1]


# In[4]:


array.shape


# In[5]:


array=np.array([[1,3,5],[2,4,6],[9,7,5]])


# In[6]:


array


# In[7]:


array.dtype


# In[8]:


array.shape


# In[9]:


array.size


# In[10]:


zeroes=np.zeros((3,3))


# In[11]:


zeroes


# In[12]:


rng=np.arange(10)


# In[13]:


rng


# In[14]:


lspace=np.linspace(1,50,10)


# In[15]:


lspace


# In[16]:


empty=np.empty((3,3))


# In[17]:


empty


# In[18]:


identityMatrix=np.identity(10)


# In[19]:


identityMatrix


# In[20]:


arr=np.arange(99)


# In[21]:


arr


# In[22]:


arr.reshape(3,33)


# In[23]:


arr.ravel()


# In[24]:


x=[[1,3,4],[3,1,0],[2,3,1]]


# In[25]:


axisarr=np.array(x)


# In[26]:


axisarr


# In[27]:


axisarr.sum(axis=0)


# In[28]:


axisarr.sum(axis=1)


# In[29]:


axisarr.T


# In[30]:


onedim=np.array([2,4,5,64])


# In[31]:


onedim.argmax()


# In[32]:


onedim.argmin()


# In[33]:


onedim.argsort()


# In[34]:


axisarr


# In[35]:


axisarr.argsort(axis=0)


# In[36]:


axisarr.argsort(axis=1)


# In[37]:


axisarr


# In[38]:


axisar=np.array([[3,1,0],[2,2,1],[3,2,1]])


# In[39]:


axisar


# In[40]:


axisarr+axisar


# In[ ]:




