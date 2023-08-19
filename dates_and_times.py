#!/usr/bin/env python
# coding: utf-8

# ## Store a Specific Date (and Time)

# In[1]:


import datetime

# Store the current date and time
dt = datetime.datetime.now()

# Store a specific date and time
dt = datetime.datetime(3, 5, 7, 12, 0, 0)

dt

#Output: datetime.datetime(3, 5, 7, 12, 0)


# ## Use the Strftime Method to Format Dates and Times as Strings

# In[11]:


# Create a datetime object
dt = datetime.datetime.now()

# Use strftime to convert the datetime object to a string in the format "YYYY-MM-DD HH:MM:SS"
dt_string = dt.strftime("%y-%m-%d %HH:%MM:%SS")

print(dt_string) 
print(type(dt_string))

#Output: 2023-08-19 19H:08M:57S
#        <class 'str'>


# ## Parse Strings into Datetime Objects

# In[12]:


string_date = "2020-01-01 12:00:00"

# Parse the string_date into a datetime object
dt = datetime.datetime.strptime(string_date, "%Y-%m-%d %H:%M:%S")

print(dt)  

string_date1 = "21 June, 2018"
date_object1 = datetime.datetime.strptime(string_date1, "%d %B, %Y")

print(date_object1)

# Output: 2020-01-01 12:00:00
#         2018-06-21 00:00:00


# ## Operations with Dates

# In[15]:


# timedelta() allows you to alter your dates by adding a delta to your
# dates (days, months, ecc..). Find the difference between two dates. 

from datetime import datetime, timedelta

date1 = datetime(2022, 1, 8)
date2 = datetime(2022, 1, 12)
difference = date2 - date1
print(difference) 

date1 += timedelta(days = 30) 
print(date1)

# Output: 4 days, 0:00:00
#         2022-02-07 00:00:00


# ## Access the Datetime Object Properties

# In[17]:


from datetime import datetime

date = datetime(2022, 12, 28, 23, 55, 59)

print("Year =", date.year)
print("Month =", date.month)
print("Hour =", date.hour)
print("Minute =", date.minute)
print("Second =", date.second)

# Output: Year = 2022
#         Month = 12
#         Hour = 23
#         Minute = 55
#         Second = 59


# ## Other Datetime Methods

# In[18]:


# convert a datetime object to a different time zone
# using the astimezone method. Return the timestamp
# for the datetime object with the timestamp() function
# and get the number of seconds since the Unix epoch.

import datetime
import pytz

# Create a timezone object for the Eastern Time zone
et = pytz.timezone("US/Eastern")

# Create a datetime object representing the current date and time in the Eastern Time zone
dt = datetime.datetime.now(et)

# Convert the datetime object to the Pacific Time zone
pt = pytz.timezone("US/Pacific")
dt_pt = dt.astimezone(pt)

print(dt)       
print(dt_pt)    

timestamp = dt_pt.timestamp()
print(timestamp)

#Output: 2023-08-19 15:30:22.362067-04:00
#        2023-08-19 12:30:22.362067-07:00
#        1692473422.362067


# In[ ]:




