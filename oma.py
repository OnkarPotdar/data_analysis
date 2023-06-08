#!/usr/bin/env python
# coding: utf-8

# In[3]:


age = 17
if (age>18):
    print('you can enter')
elif (age==18):
    print('go to hel')
else:
    print('your are in the else block')
print('ye kya he')


# In[4]:


squares = ['r','y','b']
for i,x in enumerate(squares):
    print(x)
    print(i)


# In[5]:


squares = ['red','yellow','green','purple','blue']
for i in range(0,5):
    print('before square',i,'is',squares[i])
    squares[i]='white'
    print('afteer square',i,'is',squares[i])


# In[7]:


dates = [1998,3909,3489,3490]
i = 0
year = dates[0]
while (year !=3490):
    print(year)
    i = i + 1
    year = dates[i]
print(i)
    


# In[1]:


def printStuff(Stuff):
    for i,s in enumerate(Stuff):
        print('Album',i,'Rating',s)


# In[3]:


printStuff([1,5,6,8])


# In[5]:


def ArtistNames(*names):
    for name in names:
        print(name)


# In[7]:


ArtistNames('onkar','potdar','hi')


# In[8]:


def AddDC(x):
    x = x+'DC'
    print(x)
    return(x)


# In[11]:


AddDC('AC')


# In[12]:


z = AddDC(x)


# In[16]:


def ACDC(y):
    print(Rating)
    return (Rating+y)
rating = 9


# In[17]:


ACDC()


# In[1]:


def Mult(a,b):
    c = a*b
    return (c)
    print('this is not printed')


# In[2]:


Mult(1,5)


# In[3]:


Mult(7777777777777777777,9999999999999999989898)


# In[4]:


def square(a):
    
    # Local variable b
    b = 1
    c = a * a + b
    print(a, "if you square + 1", c) 
    return(c)


# In[5]:


square(9)


# In[6]:


# Initializes Global variable  

x = 3
# Makes function call and return function a y
y = square(x)
y


# In[7]:


# Directly enter a number as parameter

square(2)


# In[9]:



# Define functions, one with return value None and other without return value.
def MJ():
    print('Michael Jackson')
    
def MJ1():
    print('Michael Jackson')
    return(None)


# In[10]:


MJ()


# In[11]:


# See the output

MJ1()


# In[12]:


print(MJ())
print(MJ1())


# In[13]:


# Define the function for combining strings

def con(a, b):
    
    
    return(a + b)


# In[14]:


# Test on the con() function

con("This ", "is")


# In[16]:


# a and b calculation block1

a1 = 4
b1 = 5
c1 = a1 + b1 + 2 * a1 * b1 - 1
if(c1 < 0):
    c1 = 0 
else:
    c1 = 5
c1


# In[17]:


a2 = 0
b2 = 0
c2 = a2 + b2 + 2 * a2 * b2 - 1
if(c2 < 0):
    c2 = 0 
else:
    c2 = 5
c2 


# In[18]:


def Equation(a,b):
    c = a + b + 2 * a * b - 1
    if(c < 0):
        c = 0 
    else:
        c = 5
    return(c) 


# In[19]:


a1 = 4
b1 = 5
c1 = Equation(a1, b1)
c1


# In[22]:


a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except:
    print("There was an error")
        


# In[27]:


ab ='print(hi onkar what is your age 18 + 5)'
eval(ab)


# In[26]:


x = 'print(45)'
eval(x)


# In[28]:


expression = 'x*(x+1)*(x+2)'
print(expression)

x = 3

result = eval(expression)
print(result)


# In[33]:


abcd = 'x*5*795*x-58'
x=9
e=eval(abcd)
print(e)


# In[3]:


import pandas as pd


# In[4]:


x = {'Name':['Rose','John','Jane','Mary'],'ID':[1,2,3,4],'Department':['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}


# In[5]:


df = pd.DataFrame(x)
df


# In[12]:


x=df[['ID']]
x


# In[2]:


t = int(input())
for i in range(t):
    A,C = map(int,input().split())
    B = A//C
    if (A//C)==int(B):
        print(B)
    else:
        print(-1)


# In[2]:


t = int(input())
for i in range(t):
    A,C = map(int,input().split())
    B = ((A+C)//2)
    if ((A+C)//2)==B:
        
        print(B)
    else:
        print(-1)


# In[7]:


t = int(input())
X,Y=map(int,input().split())
for i in range(t):
    abc=Y//2
    ab=X-Y
    ans=ab+abc
    print(ans)


# In[8]:


X,Y=map(int,input().split())

abc=Y//2
ab=X-Y
ans=ab+abc
print(ans)


# In[2]:


import pandas as pd


# In[3]:


# read the data
data=pd.read_csv("D:\General_Files\Book1.csv")


# In[4]:


data


# In[5]:


data.head()


# In[6]:


data.tail()


# In[7]:


data.sample(len(data))


# In[8]:


data.sample(10)


# In[9]:


data.columns


# In[10]:


data.info()


# In[11]:


data.describe()


# In[12]:


data.shape


# In[13]:


data1=data['sepal_length'],data['sepal_width']


# In[14]:


print(data1)


# In[15]:


slice1= data[10:21]


# In[16]:


slice1


# In[17]:


slice1.shape


# In[18]:


# loc== index name of the row.
# iloc == index integer of the row.


# In[19]:


data.iloc[2]


# In[20]:


data.loc[data['variety']=='Iris-setosa']


# In[21]:


data.loc[2]


# In[22]:


data['variety'].value_counts()


# In[23]:


print(data['sepal_length'].value_counts())


# In[24]:


# this above code shows a value how many times occurs.


# In[25]:


sum_data=data['sepal_length'].sum()


# In[26]:


sum_data


# In[27]:


sum_data1=data['sepal_length'].mean()
sum_data1


# In[28]:


sum_data2=data['sepal_length'].mode()
sum_data2


# In[29]:


sum_data3=data['sepal_length'].median()
sum_data3


# In[30]:


import numpy as np


# In[33]:


data.describe(include='all')


# In[34]:


data.describe()


# In[36]:


data.dtypes


# In[ ]:


# python is oops


# In[43]:


data.duplicated().sum()


# In[46]:


data[data.duplicated()]


# In[47]:


data.isnull()


# In[51]:


data.isnull().sum(axis=0)


# In[49]:


data.skew()


# In[61]:


data.kurt()


# In[55]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[60]:


# visulizations on target columns
plt.title('species count')
sns.countplot(data['variety'])


# In[1]:


t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    found_m = False
    found_e = True
    found_o = True
    found_w = True
    
    for c in s:
        if c in "meowMEOW":
            if c in "eE" and found_m and not found_e:
                break
            elif c in "oO" and found_e and not found_o:
                break
            elif c in "wW" and found_o and not found_w:
                break
            elif c in "mM" and not found_m:
                found_m = True
            else:
                continue
        else:
            break
    else:
        if found_m and found_e and found_o and found_w:
            print("YES")
            continue
    
    print("NO")


# In[1]:


for _ in range(int(input())):
    s = input()
    print("YES" if all(x in s for x in "mM") and "eE" in s and "oO" in s and all(x in s for x in "wW") else "NO")


# In[2]:


def max_army_power(n, powers):
    bonuses = []
    used_bonuses = set()
    total_power = 0
    for power in powers:
        if power == 0:
            if bonuses:
                bonus = bonuses.pop()
                total_power += bonus
                used_bonuses.add(bonus)
        else:
            if power not in used_bonuses:
                bonuses.append(power)
    return total_power


t = int(input())
for _ in range(t):
    n = int(input())
    powers = list(map(int, input().split()))
    print(max_army_power(n, powers))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




