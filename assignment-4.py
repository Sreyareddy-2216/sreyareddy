#!/usr/bin/env python
# coding: utf-8

#  ## ASSIGNMENT_4

# ### Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.

# In[1]:


Add_25=lambda num:num+25
Add_25(10)


# ### Write a Python program to triple all numbers of a given list of integers. Use Python map.

# In[1]:


l=[1,2,3,4,5,6,7]
list(map(lambda l:l*3,l))


# ### Write a Python program to square the elements of a list using map() function.

# In[1]:


sample_list=[4,5,2,9]
def sqr(x):
        return(x**2)
print('square of elements of given list using map() is',list(map(sqr,sample_list)))


# In[ ]:




