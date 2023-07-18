#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Student:
    def __init__(self):
        self.__name = None
        self.__rollNumber = None

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

    def getRollNumber(self):
        return self.__rollNumber
student = Student()

student.setName("John Doe")
student.setRollNumber(12345)


name = student.getName()
rollNumber = student.getRollNumber()

print(name)  
print(rollNumber) 
    


# In[ ]:




