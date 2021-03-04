# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 14:05:38 2021

@author: nemez
"""

import os
from zipfile import ZipFile
direccion = 'python_books.zip'
with ZipFile(direccion) as archivo:
    archivo.extractall()

import fitz
documento = fitz.open("Python - AWS.pdf")
print("Número de paginas:",documento.pageCount)
print("Metadatos: ",documento.metadata)
pagina = documento.loadPage(0)
texto=pagina.getText("text")
print(texto)
nl=[texto.split()]
print(nl)

for i in nl:
    print(i)
    
import fitz
documento = fitz.open("Python  Data Science Cookbook.pdf")
print("Número de paginas:",documento.pageCount)
print("Metadatos: ",documento.metadata)
pagina = documento.loadPage(0)
texto=pagina.getText("text")
print(texto)
nl=[texto.split()]
print(nl)

for j in nl:
    print (j)
    
import fitz
documento = fitz.open("Python - Finance.pdf")
print("Número de paginas:",documento.pageCount)
print("Metadatos: ",documento.metadata)
pagina = documento.loadPage(0)
texto=pagina.getText("text")
print(texto)
nl=[texto.split()]
print(nl)

for k in nl:
    print (k)



a=len(i)
b=len(j)
c=len(j)

print(a,b,c)   
ll = {a: 'Python - AWS.pdf',b: 'Python  Data Science Cookbook.pdf',c: 'Python - Finance.pdf' } 
print(ll)
cl=[a,b,c]
d=max(cl)
print(f"El texto con mas letras es ",ll[d])

