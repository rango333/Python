#!/usr/bin/env python
# coding: utf-8

# ## Introduction

# In[1]:


get_ipython().system('pip install PyPDF2')


# ## Read in a PDF

# In[2]:


import PyPDF2

# creating a pdf file object
pdfFileObj = open("example.pdf", "rb")
  
# creating a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)

# printing number of pages in pdf file
print(len(pdfReader.pages))  

# Result: 1


# ## Extract Text

# In[3]:


# creating a page object
pageObj = pdfReader.pages[0]
  
# extracting text from page
print(pageObj.extract_text())
# Result: Example table  
#         This is an example of a data table. 
#         Disability 
#         Category Participants  Ballots 
#         Completed  Ballots 
#         Incomplete/  
#         Terminated  Results  
#         Accuracy  Time to 
#         complete 
#         Blind  5 1 4 34.5%, n=1  1199 sec, n=1  
#         Low Vision  5 2 3 98.3% n=2  
#         (97.7%, n=3)  1716 sec, n=3  
#         (1934 sec, n=2)  
#         Dexterity  5 4 1 98.3%, n=4  1672.1 sec, n=4  
#         Mobility  3 3 0 95.4%, n=3  1416 sec, n=3  
 


# ## PdfWriter

# In[5]:


# Create or manipulate PDF files.
# Merge PDFs and write to to a file.

from PyPDF2 import PdfWriter

merger = PdfWriter()

for pdf in ["example.pdf", "example.pdf"]:
    merger.append(pdf)
    
merger.write("merged_pdf.pdf")
merger.close()


# ## Rotate Pages

# In[6]:


from PyPDF2 import PdfWriter, PdfReader

reader = PdfReader("sample.pdf")
writer = PdfWriter()

writer.add_page(reader.pages[0])
writer.pages[0].rotate(90)

with open("sample.pdf", "wb") as fp:
    writer.write(fp)


# ## Add Page

# In[7]:


from PyPDF2 import PdfReader, PdfWriter

# Read the input
reader = PdfReader("sample.pdf")
page = reader.pages[0]

# Scale
page.scale_by(0.5)

# Write the result to a file
writer = PdfWriter()
writer.add_page(page)
writer.write("sample.pdf")

# Result: (True, <_io.FileIO [closed]>)


# ## Encrypt PDF

# In[15]:


# Add a password to a PDF (encrypt it):

from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("example.pdf")
writer = PdfWriter()

# Add all pages to the writer
for page in reader.pages:
    writer.add_page(page)

# Add a password to the new PDF
writer.encrypt("test")

# Save the new PDF to a file
with open("encrypted-pdf.pdf", "wb") as f:
    writer.write(f)


# ## Decrypt PDF

# In[16]:


from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("encrypted-pdf.pdf")
writer = PdfWriter()

if reader.is_encrypted:
    reader.decrypt("test")

# Add all pages to the writer
for page in reader.pages:
    writer.add_page(page)

# Save the new PDF to a file
with open("decrypted-pdf.pdf", "wb") as f:
    writer.write(f)


# ## Read Metadata

# In[17]:


from PyPDF2 import PdfReader

reader = PdfReader("example.pdf")

meta = reader.metadata

print(len(reader.pages))

# All of the following could be None!
print(meta.author)
print(meta.creator)
print(meta.producer)
print(meta.subject)
print(meta.title)

# Result: 1
#         Mary
#         Acrobat PDFMaker 9.0 for Word
#         Adobe PDF Library 9.0
#         None
#         None


# In[ ]:




