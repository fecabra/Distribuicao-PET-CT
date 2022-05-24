#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import geopandas as gpd
from geopandas.tools import geocode
from geopy.geocoders import Nominatim
import pycep_correios
from shapely.geometry import Point
from geopy.extra.rate_limiter import RateLimiter
from geopy.exc import GeocoderTimedOut
import folium 
from folium import Marker
from folium.plugins import MarkerCluster


# In[2]:


url= r"~/PET_CT_Atual_Brazil.csv"
#Transform from url to csv and read it in pandas
evaluation_Data = pd.read_csv(url, sep=";", dtype=str)
evaluation_Data['CEP'] = evaluation_Data['CEP'].astype(str)          
evaluation_Data['CEP'] = evaluation_Data['CEP'].str.replace('\.0', '')
evaluation_Data['endereco']=''
pd.DataFrame(evaluation_Data)


# In[3]:


for index, row in evaluation_Data.iterrows():
    
    if row['CEP'] != 'nan':
        geolocator = Nominatim(user_agent="tester")
        endereco = pycep_correios.get_address_from_cep(row['CEP'])
        location = geolocator.geocode(endereco['logradouro'] + ", " + endereco['cidade'] + " - " + endereco['bairro'])
        evaluation_Data.loc[index,'latitude']= location.latitude
        evaluation_Data.loc[index,'longitude']= location.longitude
        
    
    elif row['CEP'] == 'nan':
        result = geocode(row['Estabelecimento'], provider="nominatim", user_agent="eu")
        evaluation_Data.loc[index,'Ponto']=str(result)


# In[4]:


pd.DataFrame(evaluation_Data)


# In[5]:


#Baixar tabela para edicao manual dos pontos nao encontrados pelo pycep do Correios
evaluation_Data.to_csv(r'~/maps2.csv')


# In[6]:


#carregartabela com edicao manual dos pontos nao encontrados pelo pycep do Correios

url2= r"~/maps2.5.csv"
evaluation_Data2 = pd.read_csv(url2, sep=";")
pd.DataFrame(evaluation_Data2)


# In[7]:


def embed_map(m, file_name):
    from IPython.display import IFrame
    m.save(file_name)
    return IFrame(file_name, width='100%', height='500px')


# In[8]:


m_6 = folium.Map(location=[-16.1237611, - 59.9219642], zoom_start=13)


for idx, row in evaluation_Data2.iterrows():
    Marker([row['latitude'], row['longitude']]).add_to(m_6)

embed_map(m_6, 'q_6.html')


# In[9]:


#carregar tabela com edicao manual dos pontos de datas de expedicao para filtro por periodo

url2= r"~/maps2.7.csv"
evaluation_Data3 = pd.read_csv(url2, sep=";")
pd.DataFrame(evaluation_Data3)


# In[10]:


evaluation_Data3['data da exped.']=pd.to_datetime(evaluation_Data3['data da exped.'], format='%d/%m/%Y')
evaluation_Data31= evaluation_Data3[evaluation_Data3['data da exped.']<'2002']
pd.DataFrame(evaluation_Data31)


# In[11]:


m_6 = folium.Map(location=[-16.1237611, - 59.9219642], zoom_start=13)


for idx, row in evaluation_Data31.iterrows():
    Marker([row['latitude'], row['longitude']]).add_to(m_6)

embed_map(m_6, 'q_6.html')


# In[12]:


evaluation_Data32= evaluation_Data3[evaluation_Data3['data da exped.']<'2006']
pd.DataFrame(evaluation_Data32)


# In[13]:


m_6 = folium.Map(location=[-16.1237611, - 59.9219642], zoom_start=13)


for idx, row in evaluation_Data32.iterrows():
    Marker([row['latitude'], row['longitude']]).add_to(m_6)

embed_map(m_6, 'q_6.html')


# In[14]:


evaluation_Data4 = evaluation_Data3[evaluation_Data3['data da exped.']<'2010']
pd.DataFrame(evaluation_Data4)


# In[15]:


m_6 = folium.Map(location=[-16.1237611, - 59.9219642], zoom_start=13)


for idx, row in evaluation_Data4.iterrows():
    Marker([row['latitude'], row['longitude']]).add_to(m_6)

embed_map(m_6, 'q_6.html')


# In[16]:


evaluation_Data5 = evaluation_Data3[evaluation_Data3['data da exped.']<'2015']
pd.DataFrame(evaluation_Data5)


# In[17]:


m_6 = folium.Map(location=[-16.1237611, - 59.9219642], zoom_start=13)


for idx, row in evaluation_Data5.iterrows():
    Marker([row['latitude'], row['longitude']]).add_to(m_6)

embed_map(m_6, 'q_6.html')


# In[18]:


evaluation_Data6 = evaluation_Data3[evaluation_Data3['data da exped.']<'2019']
pd.DataFrame(evaluation_Data6)


# In[19]:


m_6 = folium.Map(location=[-16.1237611, - 59.9219642], zoom_start=13)


for idx, row in evaluation_Data6.iterrows():
    Marker([row['latitude'], row['longitude']]).add_to(m_6)

embed_map(m_6, 'q_6.html')


# In[20]:


evaluation_Data7 = evaluation_Data3[evaluation_Data3['data da exped.']<'2021']
pd.DataFrame(evaluation_Data7)


# In[21]:


m_6 = folium.Map(location=[-16.1237611, - 59.9219642], zoom_start=4.49999)


for idx, row in evaluation_Data5.iterrows():
    Marker([row['latitude'], row['longitude']]).add_to(m_6)

    folium.CircleMarker(
        radius=100,
        location=[row['latitude'], row['longitude']],
        popup="The Waterfront",
        color="blue",
        fill=True,
        fill_color="blue"
    ).add_to(m_6)


embed_map(m_6, 'q_6.html')


# In[22]:


evaluation_Data40= evaluation_Data3.query('Cidade=="Brusque" or Cidade=="Itajai" or Cidade=="Maravilha" or Cidade=="Brasnorte" or Cidade=="Sinop" or Cidade=="Imperatriz" or Cidade=="Belem" or Cidade=="Brasilia" or Cidade=="Campo Grande" or Cidade=="Rio Petro" or Cidade=="Barretos" or Cidade=="Criciuma" or Cidade=="Montes Claros"').drop_duplicates(subset="Cidade", keep='first', inplace=False)
pd.DataFrame(evaluation_Data40)


# In[23]:


evaluation_Data41= evaluation_Data3.query('Cidade=="Londrina" or Cidade=="Passo Fundo" or Cidade=="Joao Pessoa" or Cidade=="Aracaju"  or Cidade=="Tubarao" or Cidade=="Porto Alegre" or Cidade=="Caruaru"').drop_duplicates(subset="Cidade", keep='first', inplace=False)
pd.DataFrame(evaluation_Data41)


# In[24]:


evaluation_Data42= evaluation_Data3.query('Cidade=="Sao Luis" or Cidade=="Natal" or Cidade=="Teresina" or Cidade=="Curitiba" or Cidade=="Rio de Janeiro" or Cidade=="Presidente Prudente" or Cidade=="Sao Paulo" or Cidade=="Campinas" or Cidade=="Caxias do Sul" or Cidade=="Pouso Alegre" or Cidade=="Recife" ').drop_duplicates(subset="Cidade", keep='first', inplace=False)
pd.DataFrame(evaluation_Data42)


# In[25]:


evaluation_Data43= evaluation_Data3.query('Cidade=="Jau"  ').drop_duplicates(subset="Cidade", keep='first', inplace=False)
pd.DataFrame(evaluation_Data43)


# In[26]:


evaluation_Data44= evaluation_Data3.query('Cidade=="Salvador" or Cidade=="Manaus" or Cidade=="Passa Quatro" ').drop_duplicates(subset="Cidade", keep='first', inplace=False)
pd.DataFrame(evaluation_Data44)


# In[27]:


evaluation_Data45= evaluation_Data3.query(' Cidade=="Goiania"').drop_duplicates(subset="Cidade", keep='first', inplace=False)
pd.DataFrame(evaluation_Data45)


# In[28]:


evaluation_Data46= evaluation_Data3.query('Cidade=="BeloHorizonte"').drop_duplicates(subset="Cidade", keep='first', inplace=False)
pd.DataFrame(evaluation_Data46)


# In[29]:


m_6 = folium.Map(location=[-16.1237611, - 59.9219642], zoom_start=4.49999)


for idx, row in evaluation_Data40.iterrows():
    Marker([row['latitude'], row['longitude']]).add_to(m_6)

    folium.CircleMarker(
        radius=100,
        location=[row['latitude'], row['longitude']],
        color="green",
        fill=True,
        fill_color="green"
    ).add_to(m_6)
    
for idx, row in evaluation_Data41.iterrows():
    Marker([row['latitude'], row['longitude']]).add_to(m_6)

    folium.CircleMarker(
        radius=100,
        location=[row['latitude'], row['longitude']],
        color="yellow",
        fill=True,
        fill_color="yellow"
    ).add_to(m_6)
    
for idx, row in evaluation_Data42.iterrows():
    Marker([row['latitude'], row['longitude']]).add_to(m_6)

    folium.CircleMarker(
        radius=100,
        location=[row['latitude'], row['longitude']],
        color= "orange",
        fill=True,
        fill_color= "orange"
    ).add_to(m_6)
    
for idx, row in evaluation_Data43.iterrows():
    Marker([row['latitude'], row['longitude']]).add_to(m_6)

    folium.CircleMarker(
        radius=100,
        location=[row['latitude'], row['longitude']],
        color= "blue",
        fill=True,
        fill_color= "blue"
    ).add_to(m_6)

for idx, row in evaluation_Data44.iterrows():
    Marker([row['latitude'], row['longitude']]).add_to(m_6)

    folium.CircleMarker(
        radius=100,
        location=[row['latitude'], row['longitude']],
        color= "magenta",
        fill=True,
        fill_color="magenta"
    ).add_to(m_6)
    
for idx, row in evaluation_Data45.iterrows():
    Marker([row['latitude'], row['longitude']]).add_to(m_6)

    folium.CircleMarker(
        radius=100,
        location=[row['latitude'], row['longitude']],
        color= "purple",
        fill=True,
        fill_color="purple"
    ).add_to(m_6)
    
for idx, row in evaluation_Data46.iterrows():
    Marker([row['latitude'], row['longitude']]).add_to(m_6)

    folium.CircleMarker(
        radius=100,
        location=[row['latitude'], row['longitude']],
        color="red",
        fill=True,
        fill_color="red"
    ).add_to(m_6)

embed_map(m_6, 'q_6.html')


# In[ ]:





# In[ ]:




