#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df_rent = pd.read_csv('Metro_ZORI_AllHomesPlusMultifamily_SSA.csv')


# In[3]:


# df_rent.info()


# In[4]:


df_rent.shape


# In[5]:


df_rent[df_rent['2014-01'].isna()]


# In[6]:


df_rent.RegionName.unique()


# In[7]:


df_rent = df_rent.set_index('RegionName')


# *pick 20 metro areas + US along with LinkedIn workforce report

# In[8]:


df_metro = df_rent.loc[['United States', 'Atlanta, GA', 'Austin, TX','Boston, MA','Chicago, IL','Cleveland, OH', 'Dallas-Fort Worth, TX', 'Denver, CO', 'Detroit, MI', 'Houston, TX', 'Los Angeles-Long Beach-Anaheim, CA', 'Miami-Fort Lauderdale, FL',  'Minneapolis-St Paul, MN','Nashville, TN', 'New York, NY', 'Philadelphia, PA',  'Phoenix, AZ',  'San Francisco, CA', 'Seattle, WA', 'St. Louis, MO',  'Washington, DC'  ]]


# In[9]:


df_metro = df_metro.drop(columns= ['RegionID', 'SizeRank'] )


# In[10]:


df_metro.head()


# In[11]:


df_metro['yoy'] = round(df_metro['2021-05'] / df_metro['2020-05']*100-100 , 1)
df_metro['2yoy'] = round(df_metro['2021-05'] / df_metro['2019-05']*100-100 , 1)
df_metro['5yoy'] = round(df_metro['2021-05'] / df_metro['2016-05']*100-100 , 1)
df_metro['7yoy'] = round(df_metro['2021-05'] / df_metro['2014-05']*100-100 , 1)
df_metro.head()


# In[12]:


df_metro['2021-05'].nlargest(10)


# In[13]:


df_metro.at['San Francisco, CA', 'yoy']


# In[14]:


df_metro.filter(items=['San Francisco, CA'], axis='index').plot(kind = 'bar', figsize=(10,12))


# In[15]:


dfSanFrancisco = df_metro.filter(items=['San Francisco, CA'], axis='index')


# In[16]:


dfSanFrancisco.T.to_csv("SanFranciscoZORI.csv")


# In[17]:


df_metro['yoy'].nlargest(10)


# In[18]:


df_metro['yoy'].nsmallest(5)


# In[19]:


df_metro['2yoy'].nlargest(10)


# In[20]:


df_metro['2yoy'].nsmallest(5)


# In[21]:


df_metro['5yoy'].nlargest(10)


# In[22]:


df_metro['5yoy'].nsmallest(5)


# In[23]:


df_metro['7yoy'].nlargest(10)


# In[24]:


df_metro['7yoy'].nsmallest(5)


# In[25]:


df_metroPC = df_metro.T.pct_change(1).dropna().drop(index=['yoy','2yoy','5yoy','7yoy'])


# In[26]:


df_metroPC.head()


# In[27]:


df_metroPC.plot(figsize = (20, 10))


# In[28]:


# Divide each column by "20XX-XX".／各列を"20XX-XX"で割る。
df_metroP = round(df_metro.div(df_metro["2019-05"], axis=0)*100-100, 1)
df_metroP.head()


# In[29]:


df_metroP['2021-05'].nlargest(21)


# In[30]:


sdf_metro = df_metro.T.drop(index=['yoy','2yoy','5yoy','7yoy'])


# In[31]:


get_ipython().system('pip install seaborn')


# In[32]:


import seaborn as sns
sns.set(font='DejaVu Sans')


# In[33]:


sdf_metro.plot(figsize = (12, 10))


# In[34]:


covidimpact_rent = df_metroP.T


# In[35]:


covidimpact_rent.to_csv("covid_impact_rent.csv")


# In[36]:


covidimpact_rent.drop(index=['yoy','2yoy','5yoy','7yoy']).plot(figsize = (12, 10))


# In[ ]:




