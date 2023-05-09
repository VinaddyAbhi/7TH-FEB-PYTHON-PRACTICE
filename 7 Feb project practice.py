#!/usr/bin/env python
# coding: utf-8

# ***Q1. You are writing code for a company. The requirement of the company is that you create a python
# function that will check whether the password entered by the user is correct or not. The function should
# take the password as input and return the string “Valid Password” if the entered password follows the
# below-given password guidelines else it should return “Invalid Password”.***
# 
# 
# ***Note: 1. The Password should contain at least two uppercase letters and at least two lowercase letters.
# 2. The Password should contain at least a number and three special characters.
# 3. The length of the password should be 10 characters long.***
# 
# 

# In[5]:


import re

def check_password(password):
    # Check length of password
    if len(password) != 10:
        return "Invalid Password"
    
    # Check for at least two uppercase and two lowercase letters
    if len(re.findall(r'[A-Z]', password)) < 2 or len(re.findall(r'[a-z]', password)) < 2:
        return "Invalid Password"
    
    # Check for at least one number and three special characters
    if len(re.findall(r'\d', password)) < 1 or len(re.findall(r'[^\w\s]', password)) < 3:
        return "Invalid Password"
    
    # Password meets all requirements
    return "Valid Password"


# ***Q2. Solve the below-given questions using at least one of the following:***
# 
# ***1. Lambda functioJ
# 2. Filter functioJ
# 3. Zap functioJ
# 4. List ComprehensioI***
# 
# ***B Check if the string starts with a particular letter***
# ***Check if the string is numeric***
# ***Sort a list of tuples having fruit names and their quantity.***. ***[("mango",99),("orange",80), ("grapes", 1000)-***
# ***Find the squares of numbers from 1 to 10***
# ***Find the cube root of numbers from 1 to 10***
# ***Check if a given number is even***
# ***Filter odd numbers from the given list.
# [1,2,3,4,5,6,7,8,9,10-***
# ***Sort a list of integers into positive and negative integers lists.
# [1,2,3,4,5,6,-1,-2,-3,-4,-5,0]***
# 
# 

# In[6]:


#Check if the string starts with a particular letter:


starts_with = lambda letter, string: string.startswith(letter)


# In[7]:


#Check if the string is numeric:


is_numeric = lambda string: string.isnumeric()


# In[8]:


#Sort a list of tuples having fruit names and their quantity:

fruits = [("mango",99),("orange",80), ("grapes", 1000)]
sort_fruits = lambda fruit_list: sorted(fruit_list, key=lambda x: x[1])


# In[9]:


#Find the squares of numbers from 1 to 10:

squares = lambda n: n**2
list(map(squares, range(1,11)))


# In[10]:


#Find the cube root of numbers from 1 to 10:
import math
cube_root = lambda n: math.pow(n, 1/3)
list(map(cube_root, range(1,11)))


# In[11]:


#Check if a given number is even:

is_even = lambda num: num % 2 == 0


# In[12]:


#Filter odd numbers from the given list:

numbers = [1,2,3,4,5,6,7,8,9,10]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))


# In[13]:


#Sort a list of integers into positive and negative integers lists:

numbers = [1,2,3,4,5,6,-1,-2,-3,-4,-5,0]
positive_nums = list(filter(lambda x: x > 0, numbers))
negative_nums = list(filter(lambda x: x < 0, numbers))


# In[ ]:




