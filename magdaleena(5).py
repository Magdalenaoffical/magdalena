#!/usr/bin/env python
# coding: utf-8

# In[6]:


#1
kilometers=float(input("Enter value in kilometers:"))
conv_fac= 0.621371
miles= kilometers * conv_fac
print('%0.2f kilometers is equal to % 0.2f miles' %(kilometers,miles))


# In[1]:


#3
import streamlit as st
st.header("celcius to fahrenheit")
st.write("temperature conversion")
c= st.number_input("input the temperature in celcius")
st.write("temperature in fahrenheit is ", (c*9/5)+32)


# In[5]:


#2
import time 
start =time.time()
print(23*2.3)
end = time.time()
print(end-start)


# In[6]:


from timeit import default_timer as timer
start =timer()
print(23*2.3)
end = timer()
print(end-start)


# In[9]:


m=mass
f=Gmlm2/r2=ma
Gmlm2/=g
m=gr2/G
m=(9.8m/s2)*(6.37*106m)2/ * (6.673*10-11 Nm2/kg2)


# In[ ]:




