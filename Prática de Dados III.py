#!/usr/bin/env python
# coding: utf-8

# ESTUDO E PRÁTICA DE DATAFRAME

# In[6]:


import pandas as pd


# In[13]:


df = pd.DataFrame({'Aluno': ['Marina', 'Felipe', 'Cleyton', 'Isabel'],
                   'Créditos cursados': [20, 64, 32, 24],
                   'Rendimento acadêmico': [8.55, 7.88, 8.17, 9.04],
                   'Mês de nascimento': ['novembro', 'setembro', 'janeiro', 'julho'],
                   'Curso': ['Computação', 'Estatística', 'Computação', 'Matemática']})


# In[15]:


df


# In[17]:


df.iloc[2]


# In[19]:


df['Rendimento acadêmico']


# In[22]:


df['Rendimento acadêmico'].mean()


# In[23]:


df['Rendimento acadêmico'].describe()

