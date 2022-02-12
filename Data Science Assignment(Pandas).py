#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
data=pd.read_csv("Pokemon.csv")
HP_mean=data["HP"].mean()
Speed_mean=data["Speed"].mean()
def set_HP(value):
    if value>HP_mean:
        return "High HP"
    elif value==HP_mean:
        return "Neutral HP"
    else:
        return "Low HP"
def set_Speed(value):
    if value>Speed_mean:
        return "High Speed"
    elif value==Speed_mean:
        return "Neutral Speed"
    else:
        return "Low Speed"
data["HP_High_Low"]=data["HP"].apply(set_HP)
data["Speed_High_Low"]=data["Speed"].apply(set_Speed)
data
    


# In[ ]:




