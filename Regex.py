#!/usr/bin/env python
# coding: utf-8

# ## Search Function

# In[2]:


import re

# Search for the string "cat" in the text "The cat in the hat"
text = "The cat in the hat"
x = re.search("cat", text)
print(x) # Output: <re.Match object; span=(4, 7), match='cat'>


# ## Advanced Search Function 1/2
# 

# In[1]:


import re

#Search for any three characters in the text "The cat in the hat"
text = "The cat in the hat"
x = re.search("at", text)
print(x) # Output: <re.Match object; span=(4, 7), match='cat'>


# ## Advanced Search Function 2/2

# In[3]:


import re

# Search for a digit in the text "The cost is $5."
text = "The cost is $5."
x = re.search("\d", text)
print(x) # Output: <re.Match object; span=(13, 14), match='5'>


# ## Group Function 1/2

# In[4]:


import re

# Search for a vowel in the text "The cat in the hat"
text = "The cat in the hat."
x = re.search("[aeiou]", text)
print(x.group()) # Output: e


# ## Group Function 2/2

# In[5]:


import re

# Matching a phone number
phone_number = "123-456-7890"
phone_regex = r'^\d{3}-\d{3}-\d{4}$'
x = re.search(phone_regex, phone_number)
print(x.group()) # Output: 123-456-7890


# ## SPLIT Method

# In[7]:


import re

#Split the text according to the "." in the text
text = "The cat is cute. The dog is also cute."
x = re.search("\.", text)
print(x) # Output: ['The cat is cute', ' The dog is also cute', '']


# ## Findall Method

# In[8]:


import re

#Use the Use the findall() method and print the results.() method and print the results.
text = "The cat is cute. The dog is also cute."
x = re.findall("cute", text)
print(x) # Output: ['cute', 'cute']


# ## Finditer

# In[9]:


import re
#Apply the finditer() method and print the results using a for loop
text = "The cat is cute. The dog is ugly."

x = re.finditer("(cat|dog) is (cute|ugly)", text)
for match in x:
  print(match.group(), end=' ')  # Output: cat is cute dog is ugly


# In[ ]:




