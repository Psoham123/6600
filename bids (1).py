#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# BIDS

# In[2]:


bids = pd.read_csv('bids.csv')
bids


# In[28]:


bids_copy = bids.copy()


# In[3]:


bids.shape


# In[29]:


bids_copy


# In[30]:


bids_copy.loc[bids_copy['tokenId'] == 1, 'usd'].sum()


# In[31]:


volume = bids_copy.groupby('tokenId')['usd'].sum()


# In[32]:


volume.to_frame()


# In[33]:


bids_copy.drop(['bidder', 'contract', 'transactionId'], axis=1)


# In[5]:


sales = pd.read_csv('C:/Users/hrish/OneDrive/Desktop/Computation & Visualization/Group Project/archive/sales.csv')
sales


# In[6]:


sales.shape


# In[35]:


sales_copy = sales.copy()


# In[36]:


sales_copy


# In[37]:


sales_copy.drop(['buyer','seller', 'contract', 'transactionId'], axis=1)


# In[40]:


volume_sales = sales_copy.groupby('tokenId')['usd'].sum()
#volume_sales
#volume_sales.dropna(axis = 0, inplace = True, how = 'any')
volsales = volume_sales.dropna
volume_sales.to_frame()
volume_sales.sort_values(by ='usd',ascending = False)


# In[41]:


sortdf = volsales.sort_values(by='usd',ascending = False)


# In[7]:


tokens = pd.read_csv('C:/Users/hrish/OneDrive/Desktop/Computation & Visualization/Group Project/archive/tokens.csv')
tokens


# In[43]:


tokens_copy = tokens.copy()


# In[8]:


tokens.shape


# In[44]:


tokens_copy.drop(['image','media','type','size','creator','owner','dimensions','contract','transactionId'], axis=1)


# In[45]:


print("Merged Data")
merged_df = pd.merge(tokens_copy,volume, on = 'tokenId', how = 'inner')


# In[46]:


merged_df


# In[47]:


merged_df.drop(['image','media','type','size','dimensions','creator','owner','contract','transactionId'], axis = 1)


# In[48]:


sorted_df = merged_df.sort_values(by='usd',ascending = False)


# In[49]:


sorted_df


# In[50]:


sorted_df[0:100]


# In[51]:


sorted_df.drop(['image','media','description','type','tags','size','dimensions','creator','owner','contract','transactionId'],axis=1)


# In[52]:


sorted_df[0:100]


# In[57]:


volumet100 = sorted_df.drop(['image','media','description','type','tags','size','timestamp','dimensions','creator','owner','contract','transactionId'],axis=1)
#sorted_df[0:100]


# In[58]:


vol100 = volumet100.drop(volumet100[(volumet100['usd'] == 0.000000e+00)].index, inplace=False)


# In[59]:


vol100


# In[73]:


vol100.to_excel("C:/Users/hrish/OneDrive/Desktop/Computation & Visualization/Group Project/vol100.xlsx")


# In[ ]:





# In[60]:


import pandas as pd
import matplotlib.pyplot as plt



#mean = vol100['usd'].mean()
#median = vol100['usd'].median()

fig, ax = plt.subplots(figsize = (18, 6))
ax.bar(top10volume.index, top10volume['usd'], )

ax.axhline(mean, 0, 1, color = 'red', label = 'Mean')

ax.axhline(median, 0, 1, color = 'green', label = 'Median')

ax.legend()
plt.xticks(rotation = 25, wrap = True)
plt.show()


# In[71]:


import pandas as pd
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize = (40, 15))
ax.bar(top10volume.index, top10volume['usd'])
plt.xticks(top10volume.index, top10volume.index, rotation ='horizontal')
plt.ylim(0,1450000)
#plt.ylim(bottom=0, top=150)
#mean = vol100['usd'].mean()
#ax.axhline(mean, 0, 1, color = 'red', label = 'Mean')
plt.xlabel("Token")
plt.ylabel("Volume")
plt.title("Volume of Top 10 NFTs")
plt.show()


# In[72]:


top10volume


# In[63]:


median = vol100['usd'].median()


# In[64]:


median


# In[65]:


volumet100[0:20]


# In[66]:


volumet100.set_index(['tokenId'], inplace = True,drop = False)


# In[67]:


volumet100 = volumet100.reset_index(drop=True)


# In[68]:


top10volume = volumet100[0:10]


# In[69]:


volumet100


# In[70]:


top10volume


# In[ ]:





# In[ ]:




