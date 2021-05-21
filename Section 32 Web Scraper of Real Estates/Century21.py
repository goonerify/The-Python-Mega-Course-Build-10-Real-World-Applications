#!/usr/bin/env python
# coding: utf-8

# In[64]:


import requests, re, pandas
from bs4 import BeautifulSoup


# In[107]:


r=requests.get("http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS", 
        headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c=r.content

listings=BeautifulSoup(c, "html.parser")
# listings

all=listings.find_all('div', {'class': 'propertyRow'})

re.sub('[^0-9a-zA-Z$,]+', '', all[0].find('h4', {'class': 'propPrice'}).text)

# page numbers
page_nr=soup.find_all("a", {"class": "Page"})[-1].text
page_nr


# In[90]:


l=[]
for item in all:
    d={}
    d["Address"] = re.sub('[^0-9a-zA-Z$, ]+', '', item.find_all('span', {'class': 'propAddressCollapse'})[1].text)
    d["Locality"] = re.sub('[^0-9a-zA-Z$, ]+', '', item.find_all('span', {'class': 'propAddressCollapse'})[0].text)
    d["Price"]= re.sub('[^0-9a-zA-Z$,]+', '', item.find('h4', {'class': 'propPrice'}).text)
    try:
        d["Beds"] = re.sub('[^0-9a-zA-Z$, ]+', '', item.find('span', {'class': 'infoBed'}).find('b').text)
    except:
        d["Beds"] = None
    try:
        d["Area"] = re.sub('[^0-9a-zA-Z$, ]+', '', item.find('span', {'class': 'infoSqFt'}).find('b').text)
    except:
        d["Area"] = None
    try:
        d["Full Baths"] = re.sub('[^0-9a-zA-Z$, ]+', '', item.find('span', {'class': 'infoValueFullBath'}).find('b').text)
    except:
        d["Full Baths"] = None
    try:
        d["Half Baths"] = re.sub('[^0-9a-zA-Z$, ]+', '', item.find('span', {'class': 'infoValueHalfBath'}).find('b').text)
    except:
        d["Half Baths"] = None
        
    for column_group in item.find_all("div", {"class": "columnGroup"}):
        for feature_group, feature_name in zip(column_group.find_all("span", {"class": "featureGroup"}),
                                              column_group.find_all("span", {"class": "featureName"})):
            if "Lot Size" in feature_group.text:
                d["Lot Size"] = feature_name.text
    l.append(d)


# In[91]:


len(l)


# In[92]:


df=pandas.DataFrame(l)
df


# In[93]:


df.to_csv("Output.csv")


# ### 278. Crawling Through Webpages

# In[108]:


base_url="http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/#t=0&s="
l=[]
for page in range(0, int(page_nr)*10, 10):
    r=requests.get(base_url+str(page), 
        headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    listings=soup.find_all('div', {"class": "propertyRow"})
    
    for item in listings:
        d={}
        d["Address"] = re.sub('[^0-9a-zA-Z$, ]+', '', item.find_all('span', {'class': 'propAddressCollapse'})[1].text)
        d["Locality"] = re.sub('[^0-9a-zA-Z$, ]+', '', item.find_all('span', {'class': 'propAddressCollapse'})[0].text)
        d["Price"]= re.sub('[^0-9a-zA-Z$,]+', '', item.find('h4', {'class': 'propPrice'}).text)
        try:
            d["Beds"] = re.sub('[^0-9a-zA-Z$, ]+', '', item.find('span', {'class': 'infoBed'}).find('b').text)
        except:
            d["Beds"] = None
        try:
            d["Area"] = re.sub('[^0-9a-zA-Z$, ]+', '', item.find('span', {'class': 'infoSqFt'}).find('b').text)
        except:
            d["Area"] = None
        try:
            d["Full Baths"] = re.sub('[^0-9a-zA-Z$, ]+', '', item.find('span', {'class': 'infoValueFullBath'}).find('b').text)
        except:
            d["Full Baths"] = None
        try:
            d["Half Baths"] = re.sub('[^0-9a-zA-Z$, ]+', '', item.find('span', {'class': 'infoValueHalfBath'}).find('b').text)
        except:
            d["Half Baths"] = None

        for column_group in item.find_all("div", {"class": "columnGroup"}):
            for feature_group, feature_name in zip(column_group.find_all("span", {"class": "featureGroup"}),
                                                  column_group.find_all("span", {"class": "featureName"})):
                if "Lot Size" in feature_group.text:
                    d["Lot Size"] = feature_name.text
        l.append(d)


# In[109]:


df=pandas.DataFrame(l)
df


# In[110]:


df.to_csv("Output.csv")


# In[ ]:




