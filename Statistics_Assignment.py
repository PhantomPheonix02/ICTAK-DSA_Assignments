#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[4]:


data=pd.read_csv(r'C:\Data Science-ICTAK\Datasets\Students_Performance.csv')


# In[5]:


data


# In[6]:


#1.Find out how many males and females participated in the test.
data.groupby(["gender"]).count()


# In[7]:


#2.What do you think about the students' parental level of education.
level = data.groupby(["parental level of education"]).describe()
level


# In[ ]:


#Who scores the most on average for math, reading and writing based on-i.Gender-ii.Test preparation course


# In[8]:


#On basis of Gender


# In[10]:


gndr = data.groupby(["gender"]).describe()
gndr


# In[11]:


gndr_mth = gndr['math score']
gndr_mth['mean'].nlargest()


# In[12]:


gndr_read = gndr['reading score']
gndr_read['mean'].nlargest()


# In[13]:


gndr_wri = gndr['writing score']
gndr_wri['mean'].nlargest()


# In[14]:


#On the basis of test preparation course


# In[17]:


# for math score
data.groupby(["test preparation course"])["math score"].mean()


# In[18]:


# for reading score
data.groupby(["test preparation course"])["reading score"].mean()


# In[19]:


#for writing score 
data.groupby(["test preparation course"])["writing score"].mean()


# In[20]:


#What do you think about the scoring variation for math, reading and writing based on


# In[21]:


#On the basis of Gender


# In[23]:


#to find the scoring variation we have to analyse the standard deviation using std()

#for math score

data.groupby(["gender"])["math score"].std()


# In[24]:


#for reading score

data.groupby(["gender"])["reading score"].std()


# In[25]:


#for writing score

data.groupby(["gender"])["writing score"].std()


# In[26]:


#On the basis of Test preparation course


# In[28]:


#for math score

data.groupby(["test preparation course"])["math score"].std()


# In[30]:


#for reading score

data.groupby(["test preparation course"])["reading score"].std()


# In[31]:


#for writing score

data.groupby(["test preparation course"])["writing score"].std()


# In[33]:


#The management needs your help to give bonus points to the top 25% of students based on their maths score, so how will you help the management to achieve this.

#given data set have 1000 students,so by considering 25% students means 250 students.
top_students = data.nlargest(250,'math score')
top_students


# In[1]:


#CASE STUDY


# In[2]:


#to clarify whether there is any increase in sales after stepping into digital marketing


# In[5]:


import pandas as pd
from scipy.stats import ttest_rel


# In[11]:


# Load the dataset
dat=pd.read_csv(r'C:\Data Science-ICTAK\Datasets\Sales_add.csv')


# In[12]:


dat.head()


# In[13]:


dat


# In[14]:


pre_digital_sales = df['Sales_before_digital_add(in $)']



# In[15]:


post_digital_sales = df['Sales_After_digital_add(in $)']


# In[16]:


# Perform a paired t-test
t_statistic, p_value = ttest_rel(pre_digital_sales, post_digital_sales)


# In[17]:


# Define a significance level (e.g., 0.05)
alpha = 0.05


# In[18]:


# Compare p-value with significance level
if p_value < alpha:
    print("There is a significant increase in sales after implementing digital marketing.")
else:
    print("There is no significant increase in sales after implementing digital marketing.")


# In[19]:


#company needs to check whether there is any dependency between the features “Region” and “Manager”.


# In[20]:


import pandas as pd
from scipy.stats import chi2_contingency


# In[22]:


# Create a contingency table (cross-tabulation) for the two categorical variables
contingency_table = pd.crosstab(dat['Region'], dat['Manager'])


# In[23]:


# Perform chi-squared test for independence
chi2_stat, p_val, dof, expected = chi2_contingency(contingency_table)


# In[24]:


# Print the results
print('Chi-squared statistic:', chi2_stat)
print('P-value:', p_val)


# In[25]:


# Check if the p-value is less than a chosen significance level (e.g., 0.05)
alpha = 0.05
if p_val < alpha:
    print('There is a significant dependency between Region and Manager.')
else:
    print('There is no significant dependency between Region and Manager.')


# In[ ]:




