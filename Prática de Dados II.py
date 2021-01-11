#!/usr/bin/env python
# coding: utf-8

# QUANTIDADE DE ACIDENTES AUTOMOBILÍSTICOS AO LONGO DO ANO

# In[2]:


import pandas as pd


# In[6]:


acidente_auto = pd.Series([15, 20, 12, 16, 10, 11, 12, 15, 9, 10, 12, 17], 
index = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
        'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])


# In[7]:


acidente_auto


# In[11]:


acidente_auto['janeiro']


# In[13]:


acidente_auto[0:6]


# In[15]:


acidente_auto.mean()


# In[17]:


acidente_auto.std()


# In[19]:


acidente_auto.max()


# In[21]:


acidente_auto.min()


# In[23]:


acidente_auto.describe()


# In[25]:


acidente_auto.sum()


# In[27]:


acidente_auto[6:].mean()


# In[ ]:




