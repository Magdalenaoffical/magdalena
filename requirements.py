#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
st.header("'simple web app'")
st.write("'*my app*'")
value = st.slider('val')
st.write (value,"square is" ,value*value)


# In[3]:


import streamlit as st
st.header("'looking your vote eligibility'")
age=st.number_input('what is your age')
if age>=18:
    st.write('you can vote')
else:
    st.write('you can note vote')


# In[ ]:




