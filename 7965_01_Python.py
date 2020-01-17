#!/usr/bin/env python
# coding: utf-8

# In[54]:


# import pandas, numpy
import numpy as np
import pandas as pd

# Create the required data frames by reading in the files
df_s = pd.read_excel('SaleData.xlsx')
df_i = pd.read_csv('imdb.csv',escapechar = "\\")
df_d = pd.read_csv('diamonds.csv')
df_m = pd.read_csv('movie_metadata.csv',escapechar = "\\")


# In[55]:


# Q1 Find least sales amount for each item
# has been solved as an example
def least_sales(df):
    # write code to return pandas dataframe
    ls = df.groupby(["Item"])["Sale_amt"].min().reset_index()
    return ls


# In[56]:


# Q2 compute total sales at each year X region
def sales_year_region(df):
	df['year'] = df['OrderDate'].dt.year
	syr = df.groupby(['year','Region']).sum()['Sale_amt']
	return syr


# In[57]:



# Q3 append column with no of days difference from present date to each order date
def days_diff(df,date):
	df['days_diff'] = pd.to_datetime(date) - df['OrderDate']
	return df


# In[58]:


# Q4 get dataframe with manager as first column and  salesman under them as lists in rows in second column.
def mgr_slsmn(df):
	ms = df.groupby('Manager')['SalesMan'].apply(lambda x: ','.join(set(x.dropna()))).rename('list_of_salesman').reset_index()
	return ms


# In[59]:


# Q5 For all regions find number of salesman and number of units
def slsmn_units(df):
	d1 = df.groupby(['Region'])['SalesMan'].count().rename('salesmen_count')
	d2 = df.groupby(['Region'])['Sale_amt'].sum().rename('total_sales')
	su = pd.concat([d1,d2],axis=1)
	return su


# In[60]:


# Q6 Find total sales as percentage for each manager
def sales_pct(df):
	total_sales = df.groupby(['Manager'])['Sale_amt'].sum().rename('total_sales')
	sum1 = total_sales.sum()
	sp = total_sales.apply(lambda x: x/sum1).rename('percent_sales').reset_index()
	return sp


# In[61]:


# Q7 get imdb rating for fifth movie of dataframe
def fifth_movie(df):
	fm = df.loc[4,'imdb_score']
	return fm


# In[62]:


# Q8 return titles of movies with shortest and longest run time
def movies(df):
	m = []
	m.append(df['duration'].max())
	m.append(df['duration'].min())
	return m


# In[63]:


# Q9 sort by two columns - release_date (earliest) and Imdb rating(highest to lowest)
def sort_df(df):
	sd = df.sort_values(['title_year', 'imdb_score'], ascending=[True, False])
	return sd


# In[64]:


# Q10 subset revenue more than 2 million and spent less than 1 million & duration between 30 mintues to 180 minutes
def subset_df(df):
	sd = df[(df['gross'] > 2000000) & (df['budget'] < 1000000) & (df['duration'] >= 30) & (df['duration'] <= 180)]
	return sd


# In[65]:


# Q11 count the duplicate rows of diamonds DataFrame.
def dupl_rows(df):
	dr = df.duplicated().sum()
	return dr


# In[66]:


# Q12 droping those rows where any value in a row is missing in carat and cut columns
def drop_row(df):
	dr = df.dropna(subset=['carat','cut'],how='any')
	return dr


# In[67]:


# Q13 subset only numeric columns
def sub_numeric(df):
	sn = df.select_dtypes(include=np.number)
	return sn


# In[68]:


#14. Compute volume as (x y z) when depth is greater than 60. In case of depth less than 60 default volume to 8.
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


# In[69]:


#14. Compute volume as (x y z) when depth is greater than 60. 
#In case of depth less than 60 default volume to 8. 15. Impute missing price values with mean
def impute(df):
	#df['price'].fillna(value=df['price'].mean(),inplace = True) //for change in dataframe
	im = df['price'].fillna(value=df['price'].mean())
	return im


# # Bonus Questions

# In[70]:


#Generate a report that tracks the various Genere combinations for each type year on year. 
#The result data frame should contain type, Genere_combo, year, avg_rating, min_rating, max_rating, total_run_time_mins 
def genre(df):
    df['GenreCombo']=df[df.columns[16:]].T.apply(lambda g: '|'.join(g.index[g==1]),axis=0)
    df=df.groupby(['type','year','GenreCombo'],as_index=False).agg({'imdbRating':[min,max,np.mean],'duration':np.sum})
    return df


# In[71]:


#Generate a report that captures the trend of the number of letters in movies titles over years. 
#We expect a cross tab between the year of the video release and the quantile that length fall under. 
#The results should contain year, min_length, max_length, num_videos_less_than25Percentile, num_videos_25_50Percentile , 
#num_videos_50_75Percentile, num_videos_greaterthan75Precentile
def titlelength_year(df):
    df['Title_length'] = df['wordsInTitle'].str.len()
    df['Quantile']=pd.qcut(df['Title_length'], q=4, labels=False)
    df2=pd.crosstab(df.year,df.Quantile,margins=False)
    df2["min_length"]=df.groupby(["year"])["Title_length"].min()
    df2["max_length"]=df.groupby(["year"])["Title_length"].max()
    return(df2)


# In[72]:


#In diamonds data set Using the volumne calculated above, create bins that have equal population within them. 
#Generate a report that contains cross tab between bins and cut. Represent the number under each cell as a percentage of total.
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
    df['bins'] = pd.qcut(df['volume'],4,labels = False)
    df2 = pd.crosstab(df.bins,df.cut).apply(lambda r: r/r.sum(), axis=1)
    return df2


# In[73]:


#Generate a report that tracks the Avg. imdb rating quarter on quarter, in the last 10 years, 
#for movies that are top performing. You can take the top 10% grossing movies every quarter. 
#Add the number of top performing movies under each genere in the report as well. 
import math
def imdbRating_decile(df):
    year = df['title_year'].unique()
    df['url'] = df['movie_imdb_link'].apply(lambda x: x.split('?')[0])
    b4 = pd.DataFrame()
    a = 0.1
    for i in year:
        new = df[df['title_year'] == i]
        gr = new.sort_values('gross',ascending=False).apply(lambda x : x.head(math.ceil(len(x) * a)))
        b4 = b4.append(gr)
    new = pd.merge(b4,df_i,on = 'url',how='left')
    genres = new.loc[:,'Action':'Western'].columns.tolist()
    res = new.groupby('title_year')[genres].sum()
    res['Avg_Imdb'] = new.groupby('title_year')['imdb_score'].mean()
    return(res)


# In[74]:


#Bucket the movies into deciles using the duration. 
#Generate the report that tracks various features like nomiations, wins, count, top 3 geners in each decile.
def bonus_5(df):
    df['bins'] = pd.qcut(df['duration'],10,labels = False)
    df2 = df.groupby(['bins']).agg(total_nominations = ("nrOfNominations","sum"),
                               total_wins = ("nrOfWins","sum"))
    df2['total_count'] = df.groupby(['bins'])['year'].count()
    tg = (df.groupby("bins")[df.loc[:,'Action':'Western'].columns.tolist()].sum()).T
    tg_count = pd.DataFrame(tg.apply(lambda a: a.nlargest(3).index,axis=0).transpose(),)
    tg_count.columns = ["First","Second","Third"]
    df2['Top 3 Genres'] = tg_count["First"] + "," + tg_count["Second"] + "," + tg_count["Third"]
    return df2


# In[ ]:




