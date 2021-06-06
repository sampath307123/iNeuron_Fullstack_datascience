#!/usr/bin/env python
# coding: utf-8

# In[ ]:


https://drive.google.com/file/d/1etGP85wJWsgqbsh3gX5oxc8dPKLMA1eT/view

https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv
https://raw.githubusercontent.com/justmarkham/DAT8/master/data/beer.txt
https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv
https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/datasets.csv


# In[ ]:





# In[ ]:


https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv


# In[58]:


import pandas as pd
import numpy  as np
import matplotlib as mpl
import matplotlib.pyplot as plt


# In[4]:


url_tsv = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"


# In[7]:


df_tsv = pd.read_csv( url_tsv, sep ='\t')


# In[8]:


df_tsv


# In[9]:


df_tsv.head()


# In[10]:


df_tsv.head(3)


# In[14]:


df_tsv.tail()


# In[17]:


df_tsv.tail(-11)


# In[18]:


df_tsv.tail(10)


# In[19]:


df_tsv.info()


# In[20]:


len(df_tsv)


# In[21]:


df_tsv.shape[0]


# In[23]:


df_tsv.dtypes


# In[24]:


df_tsv.describe()


# In[26]:


df_tsv.columns


# In[28]:


df_tsv.item_name


# In[29]:


df_tsv.index


# In[35]:


c = df_tsv.groupby('item_name')
c = c.sum()
c = c.sort_values(['quantity'], ascending = False)
c


# In[39]:


c.head(0)


# In[42]:


c.head(1)


# In[45]:


c1 = df_tsv.groupby('choice_description')
c1 = c1.sum()
c1 = c1.sort_values(['quantity'], ascending = False)
c1


# In[46]:


c1.head(1)


# In[62]:


price_unit_dollar = lambda x: float(x[1:-1])


# In[63]:


df_tsv.item_price = df_tsv.item_price.apply(price_unit_dollar)


# In[64]:


df_tsv


# In[66]:


revenue = (df_tsv['quantity']* df_tsv['item_price']).sum()


# In[67]:


print('Revenue was : $' + str(np.round(revenue, 2)))


# In[68]:


remove_duplicate = df_tsv.drop_duplicates(['item_price', 'quantity'])


# In[70]:


remove_duplicate


# In[71]:


filter_one_prod = remove_duplicate[remove_duplicate.quantity == 1 ]


# In[72]:


price_per_item = filter_one_prod[['item_name', 'item_price']]


# In[73]:


price_per_item.sort_values(by = "item_price", ascending=False)


# In[74]:


price_per_item.sort_values(by = "item_price", ascending=False).head(1)


# In[75]:


df_tsv[df_tsv.item_name == 'Veggie Salad Bowl']


# In[88]:





# In[ ]:





# In[173]:


url_beer = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/beer.txt"


# In[178]:


df_beer = pd.read_csv( url_beer )


# In[194]:


type(df_beer)


# In[193]:


df_beer


# In[180]:


df_beer.head()


# In[181]:


df_csv.head(7)


# In[182]:


df_beer.tail()


# In[183]:


df_beer.tail(10)


# In[184]:


df_beer.tail(-10)


# In[198]:


df_beer


# In[201]:



df_beer.groupby('name')


# In[ ]:





# In[ ]:





# In[101]:


url_crime = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv"
df_crime = pd.read_csv( url_crime )


# In[102]:


df_crime.head()


# In[103]:


df_crime.head(6)


# In[104]:


df_crime.tail(6)


# In[106]:


df_crime.Year = pd.to_datetime(df_crime.Year, format = '%Y')
df_crime.info()


# In[107]:


df_crime = df_crime.set_index('Year', drop=True)


# In[108]:


df_crime


# In[109]:


df_crime = df_crime.resample('10AS').sum()


# In[110]:


df_crime


# In[114]:


population = df_crime['Population'].resample('10AS').max()
population


# In[115]:


df_crime['Population'] = population


# In[116]:


df_crime


# In[117]:


df_crime.head()


# In[118]:


df_tmp = df_crime


# In[121]:


df_tmp[:3]


# In[122]:


df_tmp.iloc[:3]


# In[123]:


df_tmp.loc[:, ['Murder', 'Robbery']]


# In[124]:


df_tmp.loc[:, ['Murder', 'Robbery']].head()


# In[126]:


df_tmp[ ['Murder', 'Robbery']].head()


# In[133]:


df_tmp.loc[ df_tmp.index[ [3,4,5]], ['Murder', 'Robbery']] 


# In[134]:


df_tmp[df_tmp['Murder'] > 24000 ]


# In[135]:


df_tmp[df_tmp['Murder'].between(20000, 450000) ]


# In[138]:


df_tmp.groupby('Year')['Murder'].mean()


# In[139]:


df_tmp.sort_values(by=['Murder', 'Violent'], ascending=[False, True])


# In[ ]:





# In[ ]:





# In[ ]:





# In[154]:


url_vinc = 'https://vincentarelbundock.github.io/Rdatasets/csv/ggplot2/mpg.csv'


# In[155]:


df_vinc = pd.read_csv( url_vinc)


# In[156]:


df_vinc.head()


# In[157]:


df_vinc.head(-1)


# In[158]:


df_vinc.head(5)


# In[160]:


table = df_vinc.pivot_table( index='cyl', columns='model', values='year', aggfunc='mean')


# In[162]:


table

