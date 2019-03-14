#!/usr/bin/env python
# coding: utf-8

# <img src="http://cfs22.simplicdn.net/ice9/new_logo.svgz "/>
# 
# # Project 04: Movielens Dataset Analysis
# 
# You don't need to limit yourself to the number of rows/cells provided. You can add additional rows in each section to add more lines of code.
# 
# **Happy coding!**

# In[1]:


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import seaborn as sns


# In[2]:


dbmovies = pd.read_table('movies.dat',sep = '::',header = None)


# In[3]:


m_column = ['Id','Title','Genre']


# In[4]:


m_column


# In[5]:


dbmovies.columns = m_column


# In[6]:


dbmovies.head()


# In[7]:


dbmovies.nunique()


# In[8]:


dbrating = pd.read_table("ratings.dat",sep = '::',header = None)


# In[9]:


dbrating.head()


# In[10]:


dbrating.nunique()


# In[11]:


r_col = ['Id','Review','Rating',"MobileNo"]


# In[12]:


dbrating.columns = r_col


# In[13]:


dbrating.head()


# In[14]:


dbusers = pd.read_table("users.dat",sep = '::',header = None)


# In[15]:


u_col = ['Id','Gender','Age','X','occupation']


# In[16]:


dbusers.columns = u_col


# In[17]:


dbusers.nunique()


# In[18]:


dbusers.head()


# In[19]:


t_mer = pd.merge(dbmovies,dbusers, how = 'inner',on = 'Id')


# In[20]:


t_mer.head()


# In[21]:


t_mer.isnull().sum()


# In[22]:


master = pd.merge(t_mer,dbrating, how = 'inner',on = "Id")


# In[23]:


master.head()


# In[24]:


sns.countplot('Age',data = master)


# In[25]:


User_rating=master[master.Title == 'Toy Story (1995)'][['Title','Rating']]


# In[26]:


x =master.groupby(['Title']).sum()


# In[27]:


y = x.sort_values(by = ['Review'],ascending = False).head(25)


# In[28]:


Viewship = pd.DataFrame(y.Review)


# In[29]:


Viewship.head(25)


# In[30]:


master[master.Id == 2696][['Title','Rating']]


# In[31]:


master['Genre'].apply(lambda x : x.split('|')[0]).unique()


# In[32]:


master['genre'] = master['Genre'].apply(lambda x : x.split('|')[0])


# In[33]:


master.shape


# In[34]:


master.drop(labels = 'Genre',axis =1,inplace = True)


# In[35]:


master.head()


# In[36]:


x = master.values


# In[40]:


#Importing LAbelEncoder Class
from sklearn.preprocessing import LabelEncoder , OneHotEncoder
## Creating an object for LabelEncoder
labelencoder_iv = LabelEncoder()
x[:,1]=labelencoder_iv.fit_transform(x[:,1])
x[:,2]=labelencoder_iv.fit_transform(x[:,2])
x[:,9]=labelencoder_iv.fit_transform(x[:,9])

onehotencoder = OneHotEncoder(categorical_features='all')
iv= onehotencoder.fit_transform(master).toarray()


# In[38]:


# Encoding the Dependent Variable
labelencoder_dv = LabelEncoder()
dv = labelencoder_dv.fit_transform(dv)


# In[ ]:


onehotencoder = OneHotEncoder(categorical_features=[0])
iv= onehotencoder.fit_transform(iv).toarray()


# In[41]:





# In[44]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




