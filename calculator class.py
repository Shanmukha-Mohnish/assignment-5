#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Calculator:

    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def subtract(self):
        return self.a-self.b
    def multiply(self):
        return self.a*self.b
    def divide(self):
        return self.a/self.b
a=int(input("enter first number: "))
b=int(input("enter second number: "))
obj=Calculator(a,b)
choice=1
while choice!=0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice=int(input("Enter choice: "))
    if choice==1:
        print("Result: ",obj.add())
    elif choice==2:
        print("Result: ",obj.subtract())
    elif choice==3:
        print("Result: ",obj.multiply())
    elif choice==4:
        print("Result: ",obj.divide())
    elif choice==0:
        print("Exiting!")
    else:
        print("Invalid choice!!")
 
 
print()

       


# In[ ]:




