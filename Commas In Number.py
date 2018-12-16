#!/usr/bin/env python
# coding: utf-8

# In[9]:


a=list(input("Enter the number : "))
i=-3
while abs(i)<len(a):
    a.insert(i,",")
    i-=4
s= ''.join(a)
print("The Number In International System Is :",s)


# In[ ]:





# In[ ]:




