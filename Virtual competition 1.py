#!/usr/bin/env python
# coding: utf-8

# Consider the following Python dictionary `data` and Python list `labels`:
# 
# ``` python
# data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
#         'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
#         'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#         'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
# 
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# ```
# 
# **1.** Create a DataFrame `df` from this dictionary `data` which has the index `labels`.

# In[5]:


import numpy as np
import pandas as pd
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data, index=labels)


# **2.** Display a summary of the basic information about this DataFrame and its data (*hint: there is a single method that can be called on the DataFrame*).

# In[6]:


df.info()


# **3.** Return the first 3 rows of the DataFrame `df`.

# In[10]:


df.head(3)


# **4.** Display the 'animal' and 'age' columns from the DataFrame `df`

# In[11]:


df[['animal','age']]


# **5.** Display the data in rows `[3, 4, 8]` *and* in columns `['animal', 'age']'

# In[12]:


df.loc[df.index[[3, 4, 8]], ['animal', 'age']]


# **6.** Select only the rows where the number of visits is greater than 3.

# In[13]:


df[df['visits'] > 3]


# **7.** Select the rows where the age is missing, i.e. it is `NaN`.

# In[14]:


df[df['age'].isnull()]


# **8.** Select the rows where the animal is a cat *and* the age is less than 3.

# In[15]:


df[(df['animal'] == 'cat') & (df['age'] < 3)]


# **9.** Select the rows where the age is between 2 and 4 (inclusive)

# In[16]:


df[df['age'].between(2, 4)]


# **10.** Change the age in row 'f' to 1.5.

# In[19]:


df.loc['f', 'age'] = 1.5
print(df)


# **11.** Calculate the sum of all visits in `df` (i.e. the total number of visits).

# In[20]:


df['visits'].sum()


# **12.** Calculate the mean age for each different animal in `df`.

# In[21]:


df.groupby('animal')['age'].mean()


# **13.** Append a new row 'k' to `df` with your choice of values for each column. Then delete that row to return the original DataFrame.

# In[27]:


df.loc['k'] = [5.5, 'dog', 'no', 2]
print(df)


# In[26]:


df = df.drop('k')
print(df)


# **14.** Count the number of each type of animal in `df`.

# In[28]:


df['animal'].value_counts()


# **15.** Sort `df` first by the values in the 'age' in *decending* order, then by the value in the 'visits' column in *ascending* order (so row `i` should be first, and row `d` should be last).

# In[29]:


df.sort_values(by=['age', 'visits'], ascending=[False, True])


# **16.** The 'priority' column contains the values 'yes' and 'no'. Replace this column with a column of boolean values: 'yes' should be `True` and 'no' should be `False`.

# In[31]:


df['priority'] = df['priority'].map({'yes': True, 'no': False})
print(df)


# **17.** In the 'animal' column, change the 'snake' entries to 'python'.

# In[33]:


df['animal'] = df['animal'].replace('snake', 'python')
print(df)


# **18.** Load the ny-flights dataset to Python

# In[44]:


import pandas as pd
datas=pd.read_csv(r'C:\Data Science-ICTAK\Datasets\ny-flights.csv')
datas


# **19.** Which airline ID is present maximum times in the dataset

# In[48]:


datas['airline_id'].max()
datas['airline_id'].value_counts()


# **20.** Draw a plot between dep_delay and arr_delay

# In[53]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
datas.info()
sns.boxplot(x='dep_delay',y='arr_delay',data=datas)
sns.jointplot(x="dep_delay",y="arr_delay",data=datas)

