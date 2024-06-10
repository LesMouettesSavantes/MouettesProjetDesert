from functions_paysages import *
import random
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


n = 100
p0 = 0.2

#---------------------------------------- 
V = get_von_neumann_neighbors(100,3,2)
#print(len(V))
 
#------------------------------------ 
paysage  = initial_paysage(n,p0)

#---------------------- 
U = random.choice(V)
#print(U[0])
#print(U[1])
#print(paysage[U[0],U[1]])


#-------------------- 
neighbors1  = tuple(get_von_neumann_neighbors(n, 1,2))
neighbors2  = tuple(get_von_neumann_neighbors(n, 1,3))
print(type(neighbors1))

print(neighbors1 + neighbors2)
print(set(neighbors1))
    