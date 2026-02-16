#!/usr/bin/env python
# coding: utf-8

# In[44]:


import pandas as pd
import numpy as np
import ipaddress
from urllib.parse import urlparse
import re
from collections import Counter


# In[2]:


df=pd.read_csv(r"D:\Phishing_detection\Dataset\url_dataset.csv")


# In[3]:


df.head()


# In[4]:


meow=df["type"].value_counts(normalize=True)*100
meow


# In[5]:


df.shape,df["type"].unique()


# In[6]:


df[(df["type"]=="phishing")]


# In[44]:


df.isna().sum()
df[df["url"].duplicated()]


# # INFO ABOUT DATASET
# 
# - Shape((450176, 2))
# - Classes ['legitimate', 'phishing']
# - Features ['url', 'type']
# - Has no duplicated rows and nan values :)
#  

# In[ ]:


#Path to length ratio function made
from urllib.parse import urlparse
def path_to_length_ratio(url):

    print("Computing path to length ratio!")
    parsed=urlparse(url)
    total_length=len(url)
    path=parsed.path
    path_length=len(path)
    path_ratio=path_length/total_length
    print("Computed path to length ratio")
    return path_ratio
    


# In[ ]:


path_to_length_ratio("http://ecct-it.com/docmmmnn/aptgd/index.php")


# In[16]:


def length_of_url(url):
    return len(url)

print(length_of_url("http://ecct-it.com/docmmmnn/aptgd/index.php"))


# In[17]:


def special_char_ratio(url):
    special_chars = ".-@?=&_%/#"
    special_count = sum(1 for char in url if char in special_chars)
    return special_count / len(url)


# In[18]:


special_char_ratio("http://ecct-it.com/docmmmnn/aptgd/index.php")


# In[21]:


def suspicious_char_count(url):
    return sum(1 for char in url if not char.isalnum())


# In[22]:


suspicious_char_count("http://ecct-it.com/docmmmnn/aptgd/index.php")


# In[50]:


def slash_count(url):
   slash='/' 
   slash_cunt=sum(1 for char in url if char in slash)
   return slash_cunt

slash_count("http://ecct-it.com/docmmmnn/aptgd/index.php")


# In[ ]:





# In[31]:


phishing_urls=df[df["type"]=="phishing"]
urls=phishing_urls["url"].dropna().tolist()



def tokenize(url):
    url=url.lower()
    token= re.split(r'[-/?=&]',url)
    return [t for t in token if t]

all_tokens=[]
for url in urls:
    all_tokens.extend(tokenize(url=url))


# In[33]:


token_counts = Counter(all_tokens)

top_suspicious_keywords = [word for word, count in token_counts.most_common(100)]
print(top_suspicious_keywords)

stopwords = {"www", "http", "https", "com", "net", "org", "html"}
filtered_keywords = [word for word in top_suspicious_keywords if word not in stopwords]


# In[34]:


def count_suspicious_keywords(url, suspicious_keywords):
    tokens = tokenize(url)
    return sum(1 for token in tokens if token in suspicious_keywords)


# In[35]:


count_suspicious_keywords("http://ecct-it.com/docmmmnn/aptgd/index.php",suspicious_keywords=filtered_keywords)


# In[47]:


def no_dot_present(url):
   dot='.'
   dot_count=sum(1 for char in url if char in dot)
   return dot_count

print(no_dot_present("http://ecct-it.com/docmmmnn/aptgd/index.php"))


# In[38]:


#checking presence of query
def has_query(url):
    parsed = urlparse(url)
    return int(bool(parsed.query)) 


print(has_query("http://ecct-it.com/docmmmnn/aptgd/index.php"))


# In[48]:


def no_question_marks(url):
    meow='?'
    question_count= sum(1 for char in url if char in meow )
    return question_count

print(no_question_marks("http://ecct-it.com/docmmmnn/aptgd/index.php"))


# In[3]:


def countDashesInUrls(url):
    mark = '-'
    count = 0
    for i in url:
        if i == mark:
            count+=1
    return count

print(countDashesInUrls("http://ecct-it.com/docmmmnn/aptgd/index.php"))


# In[4]:


def countAtInUrls(url):
    mark = '@'
    count = 0
    for i in url:
        if i == mark:
            count+=1
    return count

print(countAtInUrls("http://ecct-it.com/docmmmnn/aptgd/index.php"))


# In[7]:


def findASymbolAtLast(url):
    if url[-1] == '/':
        return 0
    if not url[-1].isalnum():
        return 1
    return 0

print(findASymbolAtLast("http://ecct-it.com/docmmmnn/aptgd/index.php"))


# In[12]:


def checkHttpInMiddle(url):
    substr = 'http'
    url = url[4:]
    for i in range(len(url)-len(substr)+1):
        if url[i:i+len(substr)] == substr:
            return True
    return False

print(checkHttpInMiddle("http://ecct-it.com/docmmmnn/aptgd/index.php"))

    


# In[ ]:


def checkHttpInMiddle(url):
    substr = 'http'
    url = url[4:]
    for i in range(len(url)-len(substr)+1):
        if url[i:i+len(substr)] == substr:
            return True
    return False

print(checkHttpInMiddle("http://ecct-it.com/docmmmnn/aptgd/index.php"))


# In[ ]:


def has_ip_address(url):
    if not url:
        return False
    candidates = re.findall(r"(?:\d{1,3}\.){3}\d{1,3}", url)
    for candidate in candidates:
        try:
            ipaddress.ip_address(candidate)
            return True
        except ValueError:
            continue
    return False


# In[41]:


def has_unicode_chars(url):
    if not url:
        return False
    return any(ord(ch) > 127 for ch in url)


# In[ ]:


def has_port_number(url):
    if not url:
        return False
    return re.search(r":\d{1,5}\b", url) is not None


# In[43]:


print(has_ip_address("http://192.168.1.10/login"))
print(has_ip_address("http://example.com/path/10.0.0.1"))
print(has_ip_address("http://example.com"))

print(has_unicode_chars("http://example.com"))
print(has_unicode_chars("http://exämple.com"))

print(has_port_number("http://example.com:8080"))
print(has_port_number("example.com/path:1234"))
print(has_port_number("http://example.com"))


# In[ ]:




