#!/usr/bin/env python
# coding: utf-8

# In[2]:


a="Sana Jafar Sheikh"
print(a)


# ## List and its default functions
# 

# In[3]:


lst = ["1","16","apple","mango","4","8"]
print(lst)


# In[5]:


lst.append('vegetables')
print('Updated list: ', lst)


# In[6]:


language = ['French', 'English']

language1 = ['Hindi', 'Marathi']

language.extend(language1)

print('Language List:', language)


# In[7]:


systems = ['Windows', 'macOS', 'Linux', 'android']
print('Original List:', systems)

systems.reverse()

print('Updated List:', systems)


# In[8]:


animals = ['cat', 'dog', 'rabbit', 'guinea pig']

animals.remove('rabbit')

print('Updated animals list: ', animals)


# In[9]:


languages = ['Python', 'Java', 'C++', 'French', 'C']
return_value = languages.pop(3)
print('Return Value:', return_value)
print('Updated List:', languages)


# # Dictionary and its default functions

# In[10]:


person = {'name': 'Anna', 'age': '20' , 'profession':'student'}
person


# In[13]:


person.get('name')


# In[14]:


person.items()


# In[15]:


person.update({'salary': 3500.0})
print('\nAfter dictionary is updated')
person


# In[17]:


person.pop('salary')


# In[18]:


person


# In[20]:


type(person)


# # Sets and its default funstions

# In[21]:


fruits = {"apple", "banana", "cherry"}

fruits.add("orange") 

print(fruits) 


# In[22]:


fruits.clear()

print(fruits) 


# In[24]:


fruits = {"apple", "banana", "cherry"}

fruits.pop() 

print(fruits) 


# In[25]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y) 

print(z) 


# In[30]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y) 

print(z) 


# # Tuples and default methods

# In[31]:


thistuple = ("apple", "banana", "cherry")
print(thistuple[1])


# In[28]:


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])


# In[32]:


thistuple = ("apple", "banana", "cherry")
print(len(thistuple)) 


# In[33]:


tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3) 


# # Strings and its default functions

# In[34]:


txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)


# In[35]:


a = "Hello"
b = "World"
c = a + b
print(c)


# In[37]:


a = "Hello, everyone!"
print(a[1])


# In[ ]:




