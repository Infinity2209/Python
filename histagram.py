from turtle import title
import matplotlib.pyplot as plt
import numpy as np
from sqlalchemy import values
x=['Python','DAA','DSP','COA','DC','E.Economics','D.Math']
y=[85,90,60,80,50,40,100]
fig,ax =plt.subplots(figsize=(10,50))
ax.hist(x, bins=[0,1,2,3,4,5,6])
plt.show()