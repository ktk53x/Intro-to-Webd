#!/usr/bin/env python
# coding: utf-8

# In[4]:


a = list(map(int,input("Enter the list of numbers : ").split()))
def frequency(b):
    d = {}                             
    for x in b:
        if x not in d:                  
            d[x] = 1                     
        else:                           
            d[x] += 1 
    print("Frequency Of Numbers is as follows : ")
    for k in d:
        print(k,":",d[k])
frequency(a)


# In[ ]:




