#!/usr/bin/env python
# coding: utf-8

# In[1]:


#### 2. Création d'une fonction comportant des modules de gestions des exceptions
#### A partir de la fonction factorielle
def factorielle(n):
    if n== 0:
        return 1
    else:
        return n * factorielle(n-1)


# In[3]:


factorielle(5)


# In[13]:


#### Pour une chaine de caractère
from math import *
def factorielle(n):
    if (type(n) == str):
        print (" Il est impossible de saisir une chaine de caractére")
        print (" veuillez saisir des valeurs numérique")
        
#### Pour un nombre complexe 
elif (type(n) == complex): 
        print (" Nous ne pouvons pas choiri un nombre complexe")
        while (type(n) == complex): 
            
#### Pour un nombre négatif
elif (n < 0):
        print (" nous ne pouvons pas choisir un numéro négatif")
        
        if (n < 0):
            while (n<0):

#### Pour un très grand nombre
elif (len(str(n) > 10):
        print (" Nous ne pouvons pas choisir un nombre trop grand")
        
        while len(str(n) > 10):
            n = int(input("LA valeur que vous avez tapez est supérieur à 10 unités"))

#### Pour un très petit nombre 
 elif (len(str(n) < 2):
        print (" Nous ne pouvons pas choisir un nombre trop grand")
        
        while len(str(n) < 2):
            n = int(input("LA valeur que vous avez tapez est supérieur à 10 unités"))             

