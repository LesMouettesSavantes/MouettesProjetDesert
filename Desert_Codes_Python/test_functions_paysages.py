from functions_paysages import *
import random
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


n = 20
p0 = 0.2

#---------------------------------------- 
V = get_von_neumann_neighbors(100,3,2)
#print(len(V))
 
#------------------------------------ 
paysage0  = initial_paysage(n,p0)
fig0 = plot_my_paysage(paysage0,"Temps= 0")
plt.show()
#---------------------- 
U = random.choice(V)


#print(U[0])
#print(U[1])
#print(paysage[U[0],U[1]])


#-------------------- 
neighbors  = get_von_neumann_neighbors_2cells(n, 16,1,16,2)
print(neighbors)

 

    