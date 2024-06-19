import random
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import math
from functions_paysages import *


plt.close("all")
#################################################################################
####################################"" Etat initial du paysage 
#################################################################################
# -----------------définir un tableau avec l'indice de la cellule en ligne, en colonne et son etat (0 ou 1)

etats_possibles = [0,1] #   1 = V = Vegetalisé, E = Empty 
n = 100
p0 = 0.9


paysage_0 = initial_paysage(n,p0)


#------ Densité du paysage à l'instant 0 
dens0 = np.mean(paysage_0)
#------ Représentation du paysage
#plot_my_paysage(paysage_0,"Temps= 0")


####################################################################################
##########################"  TRANSITION
#####################################################################################
paysage_t  = np.copy(paysage_0)
dens =  []
dens.append(np.mean(paysage_0))

p = 0.7
q = 0.4
Tspan  = 1000

for t in range(Tspan): 
    print(t)
    paysage_tp1 = transition_EbyModel(paysage_t,n,p,q)
    paysage_t = np.copy(paysage_tp1)
    dens.append(np.mean(paysage_tp1))
    if dens[-1]==0: 
        break
    
    
print(paysage_tp1)
fig0 = plot_my_paysage(paysage_0,"Temps= 0")
figtp1 = plot_my_paysage(paysage_tp1,"Temps= Tspan")
plt.show()

plt.plot(dens)
plt.show()