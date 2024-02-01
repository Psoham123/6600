#!/usr/bin/env python
# coding: utf-8

# In[36]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns


# In[42]:


df = pd.read_csv('NFT_Top_Collections.csv')
df


# In[38]:


df.shape


# In[39]:


df.info()


# In[16]:


df.isna().sum()


# In[17]:


nft = df.copy()


# In[19]:


nft.head()


# In[23]:


new_nft = nft.drop(columns =['Category', 'Website','Logo'])
new_nft.shape


# In[29]:


new_nft.duplicated().sum()


# In[30]:


new_nft.describe()


# In[31]:


new_nft.corr()


# In[41]:


plt.subplots(figsize=(10,10))
sns.heatmap(new_nft.corr(),annot=True,linewidths = 1)
plt.show()


# In[45]:


plt.subplots(figsize=(90,15))
sns.barplot(x=new_nft.Name,y=new_nft.Owner_Asset_Ratio.sort_values(),palette = "rocket")
plt.xticks(rotation = 90)
plt.xlabel("NFT Project Name",fontsize =30)
plt.ylabel("NFT Owner-Asset Ratio",fontsize =30)
plt.title("Top 100 NFT Popularity by Owner-Asset Ratio",fontsize =50)
plt.show()

