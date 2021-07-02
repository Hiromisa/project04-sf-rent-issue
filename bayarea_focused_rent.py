#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns


# In[2]:


df = pd.read_csv("bayarea_zipcodes.csv")


# In[3]:


df.info()


# In[4]:


df2 = pd.DataFrame(df[['PO_NAME', 'ZIP']])


# In[5]:


df2.shape


# In[6]:


df2.head()


# In[7]:


df3 = pd.read_csv("Zip_ZORI_AllHomesPlusMultifamily_SSA.csv")


# In[8]:


df3.shape


# In[29]:


dfSF = df3[df3.MsaName.str.contains('San Francisco, CA') | df3.MsaName.str.contains('San Jose, CA')]  


# In[30]:


dfSF = pd.DataFrame(dfSF)


# In[31]:


#add a new column which shows change from 2020-01
dfSF['change_before_pandemic'] = dfSF['2021-05']/dfSF['2019-05']*100-100


# In[32]:


#add a new column which shows change from 2020-05
dfSF['change_yoy'] = dfSF['2021-05']/dfSF['2020-05']*100-100


# In[34]:


dfSF.shape


# In[35]:


# dfSF.columns.get_loc('RegionName')
# dfSF.columns.get_loc('2019-05')
dfSF.columns.get_loc('change_yoy')


# In[36]:


# .iloc = pick columns number （列番号を指定）
dfSF2 = pd.DataFrame(dfSF.iloc[: , [1, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]])


# In[38]:


dfSF2.shape


# In[39]:


dfSF2[dfSF2['change_yoy'].isna()]


# In[41]:


dfSF3 = df2.merge(dfSF2, left_on='ZIP' , right_on='RegionName')


# In[44]:


dfSF3.shape


# In[47]:


dfSF3 = dfSF3.set_index('ZIP')


# In[ ]:





# In[48]:


dfSF3.shape


# In[49]:


sns.set(font='DejaVu Sans')


# In[50]:


dfSF3[['2021-05', 'change_before_pandemic']].plot.scatter( x='2021-05', y='change_before_pandemic')


# In[51]:


dfSF4 = dfSF3[['PO_NAME', '2021-05', 'change_before_pandemic']]
dfSF4.to_csv("sfzip_rent.csv")


# In[ ]:




