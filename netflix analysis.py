#!/usr/bin/env python
# coding: utf-8

# In[153]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns
import datetime as dt
import warnings
warnings.filterwarnings('ignore')


# In[4]:


data=pd.read_csv("C:/Users/Oooba/Desktop/Analysis with pyhton/netflix.csv")
data


# # Data cleaning 

# In[5]:


data.info()


# In[36]:


data['date_added'] = pd.to_datetime(data['date_added'], errors='coerce', infer_datetime_format=True)


# In[37]:


data.info()


# In[6]:


data.describe()


# In[7]:


data.isna().sum()


# In[8]:


data.duplicated().sum()


# In[18]:


data.drop("show_id", axis=1)


# In[14]:


data


# In[17]:


data.shape


# # Data Manipulation

# In[100]:


types =data['type'].value_counts()
types


# In[106]:


Top_country=data["country"].value_counts().head(10)
Top_country


# In[117]:


Top_director_movie= data["director"][data["type"]=="Movie"].value_counts().sort_values(ascending=False).head(7).reset_index()
Top_director_movie.columns=["director","Movie count"]
Top_director_movie


# In[119]:


Top_director_TV= data["director"][data["type"]=="TV Show"].value_counts().sort_values(ascending=False).head(7).reset_index()
Top_director_TV.columns=["director","TV count"]
Top_director_TV


# In[120]:


Top_rating_Movie =data["rating"][data["type"]=="Movie"].value_counts().sort_values(ascending=False).head(10).reset_index()
Top_rating_Movie.columns=["rating","Movie count"]
Top_rating_Movie


# In[83]:


Top_rating_TV= data['rating'][data['type'] == 'TV Show'].value_counts().sort_values(ascending=False).head(10).reset_index()
Top_rating_TV.columns=["rating","TV count"]
Top_rating_TV


# In[89]:


data.rename(columns={'listed_in' : 'category'}, inplace=True)


# In[95]:


Top_category=data["category"].value_counts().head(10)
Top_category


# # Data Visualization

# In[156]:


plt.figure(figsize=(8,6))
plt.style.use("fivethirtyeight")
plt.hist(data['date_added'], bins=14, label='Count', color = "blue" );
plt.grid(True)
plt.title(' Date Added Years')
plt.xlabel('Years')
plt.ylabel('Count')
plt.legend()
plt.show()


# In[103]:


plt.pie(types ,labels=['Movies', 'TV Shows'], autopct='%1.1f%%', explode=[0,0.1])
plt.title('Movies & TV Shows')
plt.legend()
plt.show()


# In[139]:


Top_country.plot(kind="bar",color="blue")
plt.title("TOP COUNTRY")
plt.xlabel("Country")
plt.ylabel("Count")
plt.legend()
plt.show()


# In[137]:


Top_director_movie.plot(kind="bar",x="director",y="Movie count",color="blue")
plt.title(" TOP 7 DIRECTOR MOVIE")
plt.xlabel("Director")
plt.ylabel("Count")
plt.legend()
plt.show()


# In[136]:


Top_director_TV.plot(kind="bar",x="director",y="TV count",color="blue")
plt.title(" TOP 7 DIRECTOR TV show")
plt.xlabel("Director")
plt.ylabel("Count")
plt.legend()
plt.show()


# In[142]:


Top_rating_Movie.plot(kind="bar",x="rating",y="Movie count",color="blue")
plt.title(" TOP 10 rating Movie")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.legend()
plt.show()


# In[145]:


Top_rating_TV.plot(kind="bar",x="rating",y="TV count",color="blue")
plt.title(" TOP 10 rating TV show")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.legend()
plt.show()


# In[146]:


Top_category.plot(kind="bar",color="blue")
plt.title(" TOP 10 category")
plt.xlabel("Categoryr")
plt.ylabel("Count")
plt.legend()
plt.show()


# In[ ]:




