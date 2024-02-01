#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install pandas')
get_ipython().system('pip install requests')
get_ipython().system('pip install datetime')
get_ipython().system('pip install gql')


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[4]:


df = pd.read_csv("Data_API.csv")
df


# In[5]:


df.drop(['Smart_contract', 'Transaction_hash','Seller_address','Buyer_address','Description','Collection','Datetime_updated_seconds','Permanent_link'], axis=1)


# In[6]:


df.isna().sum()


# In[18]:


df['Category'].unique()


# In[22]:


df1 = df.groupby(['Category'])


# In[23]:


df1


# In[24]:


group_category = df.groupby('Category')
print(type(group_category))
print(group_category.groups)


# In[25]:


group_category.get_group('Art')


# In[ ]:


group_category.get_group('')


# In[27]:


category_df = df.groupby('Category').sum()


# In[30]:


category_df1 = category_df.T


# In[32]:


category_df1


# In[38]:


data = {'Art':  [6.077355e+08],
        'Collectible': [1.098362e+08],
        'Games':  [7.077352e+07],
        'Metaverse':  [6.818318e+07],
        'Other':  [2.195715e+07],
        'Utility':  [8.744349e+06],
        }

df_pie = pd.DataFrame(data)


# In[39]:


df_pie


# In[44]:


y = np.array([6.077355e+08, 1.098362e+08, 7.077352e+07, 6.818318e+07,2.195715e+07,8.744349e+06])
labels = ['Games', 'Art', 'Other', 'Collectible', 'Metaverse', 'Utility']
explode = [0.2, 0, 0, 0, 0, 0]
plt.pie(y, labels = labels, explode = explode)
plt.show()


# In[45]:


df['Market'].unique()


# In[47]:


df3 = df.groupby('Market')['Price_USD'].sum()


# In[48]:


df3


# In[49]:


df3.plot(kind="barh", fontsize=4)


# In[94]:


import matplotlib.pyplot as plt

data = {'Atomic':3.440851e+07, 'Cryptokitties': 3.143879e+07, 'Decentraland': 2.349511e+07, 'Godsunchained': 2.113385e+06, 'OpenSea':7.957740e+08}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(16, 8), sharey=True)
axs[0].bar(names, values)
plt.xticks(rotation = 90)
axs[1].scatter(names, values)
plt.xticks(rotation = 90)
axs[2].plot(names, values)
plt.xticks(rotation = 90)
fig.suptitle('Market Place Visualization in USD')


# In[60]:


market_value = [0.440851e+05,1.440851e+06,2.113385e+06,3.440851e+07,7.957740e+08]
index = ['Godsunchained', 'Cryptokitties', 'Atomic', 'Decentraland',
       'OpenSea']
df3 = pd.DataFrame({'market_value': market_value}, index=index)
ax = df3.plot.barh()


# In[ ]:




