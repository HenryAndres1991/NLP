#!/usr/bin/env python
# coding: utf-8

# <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQ-VfNtOyJbsaxu43Kztf_cv1mgBG6ZIQZEVw&usqp=CAU'>
# 
# # Procesamiento de Lenguage Natural
# 
# ## Taller #3: Web Scraping
# `Fecha de entrega: Marzo 10, 2021. (Antes del inicio de la próxima clase).`

# # Punto 1:
# 
# - `[15 pts]` Hacer Web Scraping de 10 animales en Wikipedia (en búcle)
# - `[10 pts]` Obtener el **encabezado** de cada animal
# - `[15 pts]` Obtener todos los **textos** que están en las etiquetas de negrilla.

# In[153]:


import bs4 as bs 
import urllib.request
import re


# In[42]:


import urllib.request


# In[80]:


url= ['https://es.wikipedia.org/wiki/Hydrochoerus_hydrochaeris','https://es.wikipedia.org/wiki/Ailuropoda_melanoleuca','https://es.wikipedia.org/wiki/Myrmecophaga_tridactyla','https://es.wikipedia.org/wiki/Ornithorhynchus_anatinus','https://es.wikipedia.org/wiki/Chelonoidis_carbonaria','https://es.wikipedia.org/wiki/Ramphastidae','https://es.wikipedia.org/wiki/San_bernardo_(perro)','https://es.wikipedia.org/wiki/Tar%C3%A1ntula','https://es.wikipedia.org/wiki/Tardigrada','https://es.wikipedia.org/wiki/Balaenidae']
for i in range (0,10):
    link=url[i]
    print(url[i])


# In[49]:


link=url[0]


# In[45]:


request = urllib.request.Request(link,headers={'User-Agent':'Mozilla/5.0'})
webpage = urllib.request.urlopen(request)
source = webpage.read()
webpage.close()

source
# In[46]:


title = soup.find(id="firstHeading")


# In[86]:


import requests
from bs4 import BeautifulSoup
url=['https://es.wikipedia.org/wiki/Hydrochoerus_hydrochaeris','https://es.wikipedia.org/wiki/Ailuropoda_melanoleuca','https://es.wikipedia.org/wiki/Myrmecophaga_tridactyla','https://es.wikipedia.org/wiki/Ornithorhynchus_anatinus','https://es.wikipedia.org/wiki/Chelonoidis_carbonaria','https://es.wikipedia.org/wiki/Ramphastidae','https://es.wikipedia.org/wiki/San_bernardo_(perro)','https://es.wikipedia.org/wiki/Tar%C3%A1ntula','https://es.wikipedia.org/wiki/Tardigrada','https://es.wikipedia.org/wiki/Balaenidae']

for i in range(0,10):
    response = requests.get(
    url[i]
    )
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find(id="firstHeading")
    print(title.string)


# In[143]:



for i in url:
    t=[]
    link= urllib.request.Request(i, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urllib.request.urlopen(link)
    source = webpage.read()
    
    i= bs.BeautifulSoup(source, 'html.parser')
    text1 = i.find("p").find_all("b")
    for a in text1:
        
        print(a.get_text())


# # Punto 2:
# - `[10 pts]` Usando regex, reemplazar todas las tíldes del punto anterior por un asterisco (¡Ojo, los espacios se quedan!)
# 

# In[157]:


for i in url:
    link = urllib.request.Request(i, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urllib.request.urlopen(link)
    source = webpage.read()
      
    i= bs.BeautifulSoup(source, 'html.parser')
    text1 = i.find("p").find_all("b")
    for a in text1:
        print(re.sub(r"[^a-zA-Z\s]", " (aqui va una tilde) ", a.get_text()))

