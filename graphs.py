from turtle import title
import matplotlib.pyplot as plt
import numpy as np
from sqlalchemy import values
x=['Python','DAA','DSP','COA','DC','E.Economics','D.Math']
y=[85,90,60,80,50,40,100]
plt.scatter(x,y,c='red')
plt.title("Mark of a Student")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()
data={'c':20,'c++':50,'Java':60,'Python':30}
course=list(data.keys())
values=list(data.values())
fig=plt.figure(figsize=(10,5))
plt.bar(course,values,color='blue',width=0.5)
plt.xlabel("Languages")
plt.ylabel("Values")
plt.title("Bar")
plt.show()
a=[44,22,55,188,44,133,166,107]
fig,ax =plt.subplots(figsize=(10,7))
ax.hist(a, bins=[0,25,50,100,125,150,175,200])
plt.show()