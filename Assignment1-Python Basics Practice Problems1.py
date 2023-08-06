#!/usr/bin/env python
# coding: utf-8

# In[1]:


from math import pi
r=int(input("Enter the radius of the circle:"))
print ("The area of the circle is " + str(pi * r**2))


# In[2]:


Name=input("Enter your name:")
Roll_no=int(input('Enter your Roll no:'))
Marks=input('Enter marks obtained:')
print("Name: {}\nRoll_no: {}\nMarks: {}".format(Name,Roll_no,Marks))


# In[3]:


List=[2,4,6,8]
print(str( max(List)) +' is the largest number.' )


# In[4]:


previous_num = 0
for i in range(1, 11):
    sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", sum)
    previous_num = i


# In[5]:


lower = int(input("Enter lower range limit:"))
upper = int(input("Enter upper range limit:"))
for i in range(lower, upper+1):
   if i%5==0:
      print(i)


# In[11]:


num = int(input("Enter a number: "))
if num > 1:  
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
   else:
       print(num,"is a prime number")
else:
   print(num,"is not a prime number")


# In[14]:


original_list = [1, 2, 3, 4, 5]
print("List before reverse : ",original_list)
reversed_list = []
for value in original_list:
  reversed_list = [value] + reversed_list
print("List after reverse : ", reversed_list)
 


# In[17]:


n = int(input("Enter the number of rows:"))  
for i in range(0, n):  
        for j in range(0, i + 1):    
            print("*", end="")       
        print() 


# In[18]:


num1 = 10
num2 = 14
num3 = 12
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3
print("The largest number is", largest)


# In[20]:


n=5;
for i in range(n):
    for j in range(i):
        print ('*', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('*', end="")
    print('')

