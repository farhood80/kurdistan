#!/usr/bin/env python
# coding: utf-8

# In[9]:


# importing necessary libraries 
# we use folium for viewing the cities on map

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import os
import folium



# In[10]:


# delcraing of the map ,size and starting point 

Kurdistan_map = folium.Map(
location=[32,44],
zoom_start =5,)

#here we start declaring the cities in the folium
sanandaj1 = folium.map.FeatureGroup()
urmia2 = folium.map.FeatureGroup()
kermanshah3 = folium.map.FeatureGroup()
ilam4 = folium.map.FeatureGroup()
mahabad5 = folium.map.FeatureGroup()
maku6 = folium.map.FeatureGroup()
hewler7 = folium.map.FeatureGroup()
slemani8 = folium.map.FeatureGroup()
mousl9 = folium.map.FeatureGroup()
kerkuk10 = folium.map.FeatureGroup()
duhok11 = folium.map.FeatureGroup()
shingal12 = folium.map.FeatureGroup()
halabche13 = folium.map.FeatureGroup()
khaneqin14 = folium.map.FeatureGroup()
qamislo15 = folium.map.FeatureGroup()
hasaka16 = folium.map.FeatureGroup()
giresipi17 = folium.map.FeatureGroup()
serekani18 = folium.map.FeatureGroup()
raqqa19 = folium.map.FeatureGroup()
kobani20 = folium.map.FeatureGroup()
jarablus21 = folium.map.FeatureGroup()
azaz22 = folium.map.FeatureGroup()
minbij23 = folium.map.FeatureGroup()
afrin24 = folium.map.FeatureGroup()
albab25 = folium.map.FeatureGroup()
shadadi26 = folium.map.FeatureGroup()
tilrafaat27 = folium.map.FeatureGroup()
zakho28 = folium.map.FeatureGroup()
colemerg29 = folium.map.FeatureGroup()
shirnax30 = folium.map.FeatureGroup()
van31 = folium.map.FeatureGroup()
mardin32 = folium.map.FeatureGroup()
igdir33 = folium.map.FeatureGroup()
agri34 = folium.map.FeatureGroup()
erzerum35 = folium.map.FeatureGroup()
erzican36 = folium.map.FeatureGroup()
mush37 = folium.map.FeatureGroup()
kras38 = folium.map.FeatureGroup()
amed39 = folium.map.FeatureGroup()
chewlig40 = folium.map.FeatureGroup()   
desrim41 = folium.map.FeatureGroup()
sivas42 = folium.map.FeatureGroup()
ardahan43 = folium.map.FeatureGroup()
shanliurfa44 = folium.map.FeatureGroup()
gaziantep45 = folium.map.FeatureGroup()
hatay46 = folium.map.FeatureGroup()
osmaniye47 = folium.map.FeatureGroup()    
adana48 = folium.map.FeatureGroup()
marash49 = folium.map.FeatureGroup()
malatya50 = folium.map.FeatureGroup()    
adiyaman51 = folium.map.FeatureGroup()
sirt52 = folium.map.FeatureGroup()
batman53 = folium.map.FeatureGroup()
bitlis54 = folium.map.FeatureGroup()   
bayburt55 = folium.map.FeatureGroup()    
guanshane56 = folium.map.FeatureGroup()
artivan57 = folium.map.FeatureGroup()
elazig58 = folium.map.FeatureGroup()
makhmur59 = folium.map.FeatureGroup()


# In[11]:


# creating circle around each cities based on thier geographical coordinations
# green = Eastern Kurdsitan (iranian kurdistan)
# yellow = Southern Kurdistan (iraqi Kurdistan)
# grey = Western Kurdistan (syrain kurdistan)
# red = Northern Kurdistan (turkish kurdsistan)

sanandaj1.add_child(
folium.features.CircleMarker([35.3119,46.9964],radius=7,color = "green", fill_color = "green")
)

urmia2.add_child(
folium.features.CircleMarker([37.5498,45.0786],radius=7,color = "green", fill_color = "green")
)

kermanshah3.add_child(
folium.features.CircleMarker([34.3277,47.0778],radius=7,color = "green", fill_color = "green"),

)

ilam4.add_child(
folium.features.CircleMarker([33.6350,46.4153],radius=7,color = "green", fill_color = "green"))

mahabad5.add_child(
folium.features.CircleMarker([36.7683,45.7337],radius=7,color = "green", fill_color = "green"))

maku6.add_child(
folium.features.CircleMarker([39.2916,44.4647],radius=7,color = "green", fill_color = "green")
)

hewler7.add_child(
folium.features.CircleMarker([36.1901,43.9930],radius=7,color = "yellow", fill_color = "yellow")
)

slemani8.add_child(
folium.features.CircleMarker([36.1901,43.9930],radius=7,color = "yellow", fill_color = "yellow")
)

mousl9.add_child(
folium.features.CircleMarker([35.5558,45.4351],radius=7,color = "yellow", fill_color = "yellow")
)

kerkuk10.add_child(
folium.features.CircleMarker([36.3489,43.1577],radius=7,color = "yellow", fill_color = "yellow")
)

duhok11.add_child(
folium.features.CircleMarker([35.4666,44.3799],radius=7,color = "yellow", fill_color = "yellow")
)

shingal12.add_child(
folium.features.CircleMarker([36.3142,41.8624],radius=7,color = "yellow", fill_color = "yellow")
)

halabche13.add_child(
folium.features.CircleMarker([35.1833 ,45.9833],radius=7,color = "yellow", fill_color = "yellow")
)

khaneqin14.add_child(
folium.features.CircleMarker([34.3543,45.3839],radius=7,color = "yellow", fill_color = "yellow")
)

qamislo15.add_child(
folium.features.CircleMarker([36.8190,38.0076],radius=7,color = "grey", fill_color = "grey")
)

hasaka16.add_child(
folium.features.CircleMarker([37.0549,41.2282],radius=7,color = "grey", fill_color = "grey")
)

giresipi17.add_child(
folium.features.CircleMarker([36.5079,40.7463],radius=7,color = "grey", fill_color = "grey")
)

serekani18.add_child(
folium.features.CircleMarker([36.6919,38.9512],radius=7,color = "grey", fill_color = "grey")
)

raqqa19.add_child(
folium.features.CircleMarker([36.8481,40.0787],radius=7,color = "grey", fill_color = "grey")
)

kobani20.add_child(
folium.features.CircleMarker([35.9594,38.9981],radius=7,color = "grey", fill_color = "grey")
)

jarablus21.add_child(
folium.features.CircleMarker([36.8903,38.3500],radius=7,color = "grey", fill_color = "grey")
)

azaz22.add_child(
folium.features.CircleMarker([36.5868,37.0481],radius=7,color = "grey", fill_color = "grey")
)

minbij23.add_child(
folium.features.CircleMarker([36.5353,37.9679],radius=7,color = "grey", fill_color = "grey")
)

afrin24.add_child(
folium.features.CircleMarker([36.5123, 36.8654],radius=7,color = "grey", fill_color = "grey")
)

albab25.add_child(
folium.features.CircleMarker([36.3721,37.5161],radius=7,color = "grey", fill_color = "grey")
)
shadadi26.add_child(
folium.features.CircleMarker([36.0558, 40.7311],radius=7,color = "grey", fill_color = "grey")
)

tilrafaat27.add_child(
folium.features.CircleMarker([36.4674,37.0960],radius=7,color = "grey", fill_color = "grey")
)

zakho28.add_child(
folium.features.CircleMarker([37.1505, 42.6727],radius=7,color = "yellow", fill_color = "yellow")
)

colemerg29.add_child(
folium.features.CircleMarker([37.5774,43.7368],radius=7,color = "red", fill_color = "red")
)

shirnax30 .add_child(
folium.features.CircleMarker([37.5190,42.4537],radius=7,color = "red", fill_color = "red")
)


van31.add_child(
folium.features.CircleMarker([38.3009,43.2231],radius=7,color = "red", fill_color = "red")
)

mardin32.add_child(
folium.features.CircleMarker([37.3129,40.7340],radius=7,color = "red", fill_color = "red")
)

igdir33.add_child(
folium.features.CircleMarker([37.9201,44.0436],radius=7,color = "red", fill_color = "red")
)

agri34.add_child(
folium.features.CircleMarker([39.7191,43.0506],radius=7,color = "red", fill_color = "red")
)

erzerum35.add_child(
folium.features.CircleMarker([39.9055,41.2658],radius=7,color = "red", fill_color = "red")
)

erzican36.add_child(
folium.features.CircleMarker([39.7468,39.4911],radius=7,color = "red", fill_color = "red")
)

mush37.add_child(
folium.features.CircleMarker([38.7346,41.4910],radius=7,color = "red", fill_color = "red")
)

kras38.add_child(
folium.features.CircleMarker([40.6013,43.0975],radius=7,color = "red", fill_color = "red")
)

amed39.add_child(
folium.features.CircleMarker([37.9250,40.2110],radius=7,color = "red", fill_color = "red")
)

chewlig40.add_child(
folium.features.CircleMarker([38.8855,40.4966],radius=7,color = "red", fill_color = "red")
)

desrim41.add_child(
folium.features.CircleMarker([39.1062,39.5483],radius=7,color = "red", fill_color = "red")
)

sivas42.add_child(
folium.features.CircleMarker([39.7505,37.015],radius=7,color = "red", fill_color = "red")
)

ardahan43.add_child(
folium.features.CircleMarker([41.1130,42.7023],radius=7,color = "red", fill_color = "red")
)

shanliurfa44.add_child(
folium.features.CircleMarker([37.1674,38.7955],radius=7,color = "red", fill_color = "red")
)

gaziantep45.add_child(
folium.features.CircleMarker([37.0660,37.3781],radius=7,color = "red", fill_color = "red")
)

hatay46.add_child(
folium.features.CircleMarker([36.2023,36.1613],radius=7,color = "red", fill_color = "red")
)

osmaniye47.add_child(
folium.features.CircleMarker([37.0746,36.2464],radius=7,color = "red", fill_color = "red")
)

adana48.add_child(
folium.features.CircleMarker([36.9914,35.3308],radius=7,color = "red", fill_color = "red")
)

marash49.add_child(
folium.features.CircleMarker([37.5753,36.9228],radius=7,color = "red", fill_color = "red")
)

malatya50.add_child(
folium.features.CircleMarker([38.3554,38.3335],radius=7,color = "red", fill_color = "red")
)

adiyaman51.add_child(
folium.features.CircleMarker([37.7636,38.2773],radius=7,color = "red", fill_color = "red")
)

sirt52.add_child(
folium.features.CircleMarker([37.9274,41.9420],radius=7,color = "red", fill_color = "red")
)

batman53.add_child(
folium.features.CircleMarker([37.8895,41.1293],radius=7,color = "red", fill_color = "red")
)

bitlis54.add_child(
folium.features.CircleMarker([38.4006,42.1095],radius=7,color = "red", fill_color = "red")
)

bayburt55.add_child(
folium.features.CircleMarker([40.2603,40.2280],radius=7,color = "red", fill_color = "red")
)

guanshane56.add_child(
folium.features.CircleMarker([40.4608,39.4803],radius=7,color = "red", fill_color = "red")
)

artivan57.add_child(
folium.features.CircleMarker([41.1809,41.8208],radius=7,color = "red", fill_color = "red")
)

elazig58.add_child(
folium.features.CircleMarker([38.6748,39.2225],radius=7,color = "red", fill_color = "red")
)

makhmur59.add_child(
folium.features.CircleMarker([35.7750,43.5810],radius=7,color = "yellow", fill_color = "yellow")
)


# In[12]:


# adding the cities on the folium map 

Kurdistan_map.add_child(sanandaj1)
Kurdistan_map.add_child(urmia2)
Kurdistan_map.add_child(kermanshah3)
Kurdistan_map.add_child(ilam4)
Kurdistan_map.add_child(mahabad5)
Kurdistan_map.add_child(maku6)
Kurdistan_map.add_child(hewler7)
Kurdistan_map.add_child(slemani8)
Kurdistan_map.add_child(mousl9)
Kurdistan_map.add_child(kerkuk10)
Kurdistan_map.add_child(duhok11)
Kurdistan_map.add_child(shingal12)
Kurdistan_map.add_child(halabche13)
Kurdistan_map.add_child(khaneqin14)
Kurdistan_map.add_child(qamislo15)
Kurdistan_map.add_child(hasaka16)
Kurdistan_map.add_child(giresipi17)
Kurdistan_map.add_child(serekani18)
Kurdistan_map.add_child(raqqa19)
Kurdistan_map.add_child(kobani20)
Kurdistan_map.add_child(jarablus21)
Kurdistan_map.add_child(azaz22)
Kurdistan_map.add_child(minbij23)
Kurdistan_map.add_child(afrin24)
Kurdistan_map.add_child(albab25)
Kurdistan_map.add_child(shadadi26)
Kurdistan_map.add_child(tilrafaat27)
Kurdistan_map.add_child(zakho28)
Kurdistan_map.add_child(colemerg29)
Kurdistan_map.add_child(shirnax30)
Kurdistan_map.add_child(van31)
Kurdistan_map.add_child(mardin32)
Kurdistan_map.add_child(igdir33)
Kurdistan_map.add_child(agri34)
Kurdistan_map.add_child(erzerum35)
Kurdistan_map.add_child(erzican36)
Kurdistan_map.add_child(mush37)
Kurdistan_map.add_child(kras38)
Kurdistan_map.add_child(amed39)
Kurdistan_map.add_child(chewlig40)
Kurdistan_map.add_child(desrim41)
Kurdistan_map.add_child(sivas42)
Kurdistan_map.add_child(ardahan43)
Kurdistan_map.add_child(shanliurfa44)
Kurdistan_map.add_child(gaziantep45)
Kurdistan_map.add_child(hatay46)
Kurdistan_map.add_child(osmaniye47)
Kurdistan_map.add_child(adana48)
Kurdistan_map.add_child(marash49)
Kurdistan_map.add_child(malatya50)
Kurdistan_map.add_child(adiyaman51)
Kurdistan_map.add_child(sirt52)
Kurdistan_map.add_child(batman53)
Kurdistan_map.add_child(bitlis54)
Kurdistan_map.add_child(bayburt55)
Kurdistan_map.add_child(guanshane56)
Kurdistan_map.add_child(artivan57)
Kurdistan_map.add_child(elazig58)
Kurdistan_map.add_child(makhmur59)


# In[15]:


# creating popup for each cities by using geographical coordinations and wrining thier name 

folium.Marker([35.3119,46.9964], popup = 'sanandaj').add_to(Kurdistan_map)
folium.Marker([37.5498,45.0786], popup = 'urmia').add_to(Kurdistan_map)
folium.Marker([34.3277,47.0778], popup = 'kermanshah').add_to(Kurdistan_map)
folium.Marker([33.6350,46.4153], popup = 'ilam').add_to(Kurdistan_map)
folium.Marker([36.7683,45.7337], popup = 'mahabad').add_to(Kurdistan_map)
folium.Marker([39.2916,44.4647], popup = 'maku').add_to(Kurdistan_map)
folium.Marker([36.1901,43.9930], popup = 'hewler').add_to(Kurdistan_map)
folium.Marker([35.5558,45.4351], popup = 'slemani').add_to(Kurdistan_map)
folium.Marker([36.3489,43.1577], popup = 'mousl').add_to(Kurdistan_map)
folium.Marker([35.4666,44.3799], popup = 'kerkuk').add_to(Kurdistan_map)
folium.Marker([36.8632,42.9885], popup = 'duhok').add_to(Kurdistan_map)
folium.Marker([36.3142,41.8624], popup = 'shingal').add_to(Kurdistan_map)
folium.Marker([35.1655,45.9896], popup = 'halabche').add_to(Kurdistan_map)
folium.Marker([34.3543,45.3839], popup = 'khaneqin').add_to(Kurdistan_map)
folium.Marker([37.0549,41.2282], popup = 'qamislo').add_to(Kurdistan_map)
folium.Marker([36.5079,40.7463], popup = 'hasaka').add_to(Kurdistan_map)
folium.Marker([36.6919,38.9512], popup = 'gire sipi').add_to(Kurdistan_map)
folium.Marker([36.8481,40.0787], popup = 'serekani').add_to(Kurdistan_map)
folium.Marker([35.9594,38.9981], popup = 'raqqa').add_to(Kurdistan_map)
folium.Marker([36.8903,38.3500], popup = 'kobani').add_to(Kurdistan_map)
folium.Marker([36.8190,38.0076], popup = 'jarablus').add_to(Kurdistan_map)
folium.Marker([36.5868,37.0481], popup = 'azaz').add_to(Kurdistan_map)
folium.Marker([36.4674,37.0960], popup = 'tel rifat').add_to(Kurdistan_map)
folium.Marker([36.5353,37.9679], popup = 'minbij').add_to(Kurdistan_map)
folium.Marker([36.5123, 36.8654], popup = 'afrin').add_to(Kurdistan_map)
folium.Marker([36.3721,37.5161], popup = 'al bab').add_to(Kurdistan_map)
folium.Marker([36.0558, 40.7311], popup = 'shadadi').add_to(Kurdistan_map)
folium.Marker([37.1505, 42.6727], popup = 'zakho').add_to(Kurdistan_map)
folium.Marker([37.5774,43.7368], popup = 'colemerg').add_to(Kurdistan_map)
folium.Marker([37.5190,42.4537], popup = 'shirnax').add_to(Kurdistan_map)
folium.Marker([38.3009,43.2231], popup = 'van').add_to(Kurdistan_map)
folium.Marker([37.3129,40.7340], popup = 'mardin').add_to(Kurdistan_map)
folium.Marker([39.9201,44.0436], popup = 'igdir').add_to(Kurdistan_map)
folium.Marker([39.7191,43.0506], popup = 'agri').add_to(Kurdistan_map)
folium.Marker([39.9055,41.2658], popup = 'erzerum').add_to(Kurdistan_map)
folium.Marker([39.7468,39.4911], popup = 'erzican').add_to(Kurdistan_map)
folium.Marker([38.7346,41.4910], popup = 'mush').add_to(Kurdistan_map)
folium.Marker([40.6013,43.0975], popup = 'kras').add_to(Kurdistan_map)
folium.Marker([37.9250,40.2110], popup = 'amed').add_to(Kurdistan_map)
folium.Marker([38.8855,40.4966], popup = 'chewlig').add_to(Kurdistan_map)
folium.Marker([39.1062,39.5483], popup = 'desrim').add_to(Kurdistan_map)
folium.Marker([39.7505,37.015], popup = 'sivas').add_to(Kurdistan_map)
folium.Marker([41.1130,42.7023], popup = 'ardahan').add_to(Kurdistan_map)
folium.Marker([37.1674,38.7955], popup = 'shanliurfa').add_to(Kurdistan_map)
folium.Marker([37.0660,37.3781], popup = 'gaziantep').add_to(Kurdistan_map)
folium.Marker([36.2023,36.1613], popup = 'hatay').add_to(Kurdistan_map)
folium.Marker([37.0746,36.2464], popup = 'osmaniye').add_to(Kurdistan_map)
folium.Marker([36.9914,35.3308], popup = 'adana').add_to(Kurdistan_map)
folium.Marker([37.5753,36.9228], popup = 'marash').add_to(Kurdistan_map)
folium.Marker([38.3554,38.3335], popup = 'malatya').add_to(Kurdistan_map)
folium.Marker([37.7636,38.2773], popup = 'adiyaman').add_to(Kurdistan_map)
folium.Marker([37.9274,41.9420], popup = 'sirt').add_to(Kurdistan_map)
folium.Marker([37.8895,41.1293], popup = 'batman').add_to(Kurdistan_map)
folium.Marker([38.4006,42.1095], popup = 'bitlis').add_to(Kurdistan_map)
folium.Marker([40.2603,40.2280], popup = 'bayburt').add_to(Kurdistan_map)
folium.Marker([40.4608,39.4803], popup = 'guanshane').add_to(Kurdistan_map)
folium.Marker([41.1809,41.8208], popup = 'artivan').add_to(Kurdistan_map)
folium.Marker([38.6748,39.2225], popup = 'elazig').add_to(Kurdistan_map)
folium.Marker([35.7750,43.5810], popup = 'mekhmur').add_to(Kurdistan_map)


# In[14]:


# biji kurdistan
print("Ez vê nexşeya xweş diyarî gelê kurd yê serketî dikim!")

#showing the map 
Kurdistan_map




# In[ ]:




