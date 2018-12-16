#!/usr/bin/env python
# coding: utf-8

# In[5]:


a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
c=min(a,b)
i=2
hcf=1
while i<=c:
    if a%i==0 and b%i==0:
        hcf=i
    i+=1
print("The GCD of the following number is : ",hcf)


# In[ ]:




