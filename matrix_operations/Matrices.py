#!/usr/bin/env python
# coding: utf-8

# In[102]:


class Matrix:
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y
    
    def add(self):
        result = []
        for row in range(len(self.X)):
            result.append([x+y for x,y in zip(self.X[row], self.Y[row])])
            
        return result 
    
    def subtract(self):
        result = []
        for row in range(len(self.X)):
            result.append([x-y for x,y in zip(self.X[row], self.Y[row])])
            
        return result
    
    def multiply(self):
        rows_dim = len(self.X)
        cols_dim = len(self.Y[0])
        
        # Creating an empty nested list with zeros
        result = []
        for i in range(rows_dim): 

            # Append an empty sublist inside the list 
            result.append([]) 

            for j in range(cols_dim): 
                result[i].append(0) 
                
        # Populating the nested list with product of matrices       
        for i in range(len(self.X)):
           # iterate through columns of Y
           for j in range(len(self.Y[0])):
               # iterate through rows of Y
               for k in range(len(self.Y)):
                   result[i][j] += self.X[i][k] * self.Y[k][j]
                
        return result

