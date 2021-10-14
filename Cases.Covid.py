#!/usr/bin/env python
# coding: utf-8

# # Visualisasi data Covid.19 Indonesia dan Rusia

# In[ ]:


import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('covid.19.csv')
df


# In[4]:


Cases = df[df['Country/Region'] == 'Indonesia']
Cases 


# In[12]:


Cases1 = df[df['Country/Region'] == 'Indonesia']
Cases1


# In[14]:


CasesInd = Cases1[Cases1['Confirmed']>0]
CasesInd


# In[16]:


Cases2 = df[df['Country/Region'] == 'Russia']
Cases2


# In[17]:


CasesRus = Cases2[Cases2['Confirmed']>0]
CasesRus


# In[20]:


CasesInd['Date'] = pd.to_datetime(CasesInd['Date'])
CasesRus['Date'] = pd.to_datetime(CasesRus['Date'])
CasesInd.head()


# In[32]:


CasesInd['BaseDate'] = pd.to_datetime('2020-03-02')
CasesInd.head()


# In[33]:


CasesRus['BaseDate'] = pd.to_datetime('2020-01-31')
CasesRus.head()


# In[36]:


CasesInd['HariKe'] = CasesInd['Date'] - CasesInd['BaseDate']
CasesRus['HariKe'] = CasesRus['Date'] - CasesRus['BaseDate']
CasesInd.head()


# In[37]:


CasesInd.HariKe = CasesInd.HariKe/pd.Timedelta(1, unit='d')


# In[38]:


CasesInd.head()


# In[40]:


CasesRus.HariKe = CasesRus.HariKe/pd.Timedelta(1, unit='d')


# In[42]:


CasesRus.head()


# In[44]:


plt.plot(CasesInd.HariKe, CasesInd.Confirmed)
plt.plot(CasesRus.HariKe, CasesRus.Confirmed)
plt.xlabel('Hari Ke-')
plt.ylabel('Jumlah Kasus')
plt.legend(['Indonesia', 'Rusia'])
plt.title('Jumlah Perbandingan Kasus Covid 19 Indonesia dan Rusia')
plt.show()

