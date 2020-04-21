#!/usr/bin/env python
# coding: utf-8

import pandas as pd



full_data = pd.read_csv("/Users/oliverbains/Documents/Important/COVIDTesting/owid-curl.csv")
germany = full_data[full_data["iso_code"] == "DEU"]


# In[3]:


germany = germany.drop(labels=["new_tests", "new_tests_per_thousand"], axis=1)
germany = germany.set_index("date")
germany.head(10)


# In[4]:


germany.to_csv("/Users/oliverbains/Documents/Important/COVIDTesting/germany.csv")



europeinfo = pd.read_csv("/Users/oliverbains/Documents/Important/COVIDTesting/EuropeanCountries.csv").drop("Country", axis=1)
europeinfo.head()


# In[6]:


continent = full_data.merge(europeinfo, how="left", on="iso_code")
continent.head()


# In[7]:


europe = continent[continent["Continent"] == 4]
europe.head()


# In[8]:



# we can drop the following columns as we will not use them in our final analysis. 
europe = europe.drop(axis = 1, labels=["total_tests", "new_tests", "total_tests_per_thousand", 
                    "new_tests_per_thousand", "tests_units"])


# In[9]:


# we can fill the na values with 0s, as they are instances where the count is 0 (rather than missing data)
europe = europe.fillna(0)


# In[10]:


europe.to_csv("/Users/oliverbains/Documents/Important/COVIDTesting/europe.csv")


