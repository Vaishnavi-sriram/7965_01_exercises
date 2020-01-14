#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import pandas, numpy
import numpy as np
import pandas as pd

# Create the required data frames by reading in the files
df_s = pd.read_excel('SaleData.xlsx')
df_i = pd.read_csv('imdb.csv',escapechar = "\\")
df_d = pd.read_csv('diamonds.csv')
df_m = pd.read_csv('movie_metadata.csv')


# In[2]:


# Q1 Find least sales amount for each item
# has been solved as an example
def least_sales(df):
    # write code to return pandas dataframe
    ls = df.groupby(["Item"])["Sale_amt"].min().reset_index()
    return ls


# In[3]:


# Q2 compute total sales at each year X region
def sales_year_region(df):
	df['year'] = df['OrderDate'].dt.year
	syr = df.groupby(['year','Region']).sum()['Sale_amt']
	return syr


# In[4]:



# Q3 append column with no of days difference from present date to each order date
def days_diff(df):
	df['days_diff'] = pd.to_datetime(date.today()) - df['OrderDate']
	return df


# In[5]:


# Q4 get dataframe with manager as first column and  salesman under them as lists in rows in second column.
def mgr_slsmn(df):
	ms = df.groupby('Manager')['SalesMan'].apply(lambda x: ','.join(set(x.dropna()))).rename('list_of_salesman').reset_index()
	return ms


# In[6]:


# Q5 For all regions find number of salesman and number of units
def slsmn_units(df):
	d1 = df.groupby(['Region'])['SalesMan'].count().rename('salesmen_count')
	d2 = df.groupby(['Region'])['Sale_amt'].sum().rename('total_sales')
	su = pd.concat([d1,d2],axis=1)
	return su


# In[7]:


# Q6 Find total sales as percentage for each manager
def sales_pct(df):
	total_sales = df.groupby(['Manager'])['Sale_amt'].sum().rename('total_sales')
	sum1 = total_sales.sum()
	sp = total_sales.apply(lambda x: x/sum1).rename('percent_sales').reset_index()
	return sp


# In[8]:


# Q7 get imdb rating for fifth movie of dataframe
def fifth_movie(df):
	fm = df.loc[4,'imdb_score']
	return fm


# In[9]:


# Q8 return titles of movies with shortest and longest run time
def movies(df):
	m = []
	m.append(df['duration'].max())
	m.append(df['duration'].min())
	return m


# In[10]:


# Q9 sort by two columns - release_date (earliest) and Imdb rating(highest to lowest)
def sort_df(df):
	sd = df.sort_values(['title_year', 'imdb_score'], ascending=[True, False])
	return sd


# In[11]:


# Q10 subset revenue more than 2 million and spent less than 1 million & duration between 30 mintues to 180 minutes
def subset_df(df):
	sd = df[(df['gross'] > 2000000) & (df['budget'] < 1000000) & (df['duration'] >= 30) & (df['duration'] <= 180)]
	return sd


# In[12]:


# Q11 count the duplicate rows of diamonds DataFrame.
def dupl_rows(df):
	dr = df.duplicated().sum()
	return dr


# In[13]:


# Q12 droping those rows where any value in a row is missing in carat and cut columns
def drop_row(df):
	dr = df.dropna(subset=['carat','cut'],how='any')
	return dr


# In[14]:


# Q13 subset only numeric columns
def sub_numeric(df):
	sn = df.select_dtypes(include=np.number)
	return sn


# In[16]:


def vol(df):
    vol = []
    for i in range(len(df)):
        if(df['depth'][i] > 60):
            if(df['z'][i] == 'None'):
                vol.append(np.nan)
            else:
                vol.append(float(df['x'][i])*float(df['y'][i])*float(df['z'][i]))
        else:
            vol.append(8)
    df['volume'] = vol
    return df


# In[ ]:




