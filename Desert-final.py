
import random
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import math
from functions_paysages import plot_my_paysage
from functions_paysages import get_von_neumann_neighbors

#################################################################################
####################################"" Etat initial du paysage 
#################################################################################
# -----------------définir un tableau avec l'indice de la cellule en ligne, en colonne et son etat (0 ou 1)

etats_possibles = [0,1] #   1 = V = Vegetalisé, E = Empty 
n = 100 
p0 = 0.2





#------ Densité du paysage à l'instant 0 
dens0 = np.mean(paysage_0)
#------ Représentation du paysage
plot_my_paysage(paysage_0,"Temps= 0")


####################################################################################
##########################"  TRANSITION
#####################################################################################
paysage_t  = paysage_0
paysage_tp1  = paysage_t

p=0.1
q= 0.3
n=2
for i in range(n):
    for j in range(n):
        if paysage_t[i,j] == 1:
            Vois_ij  = get_von_neumann_neighbors(n,i,j)  
            U_ij = random.choice(Vois_ij)
            if paysage_t[U_ij[0],U_ij[1]]==0: 
                Zp = np.random.binomial(1,p)
                if Zp == 1 : #'Recruitment'
                    paysage_tp1[U_ij[0],U_ij[1]] = 1 
                elif Zp == 0 : #'Mortality'
                    paysage_tp1[i,j] = 0
            elif paysage_t[U_ij[0],U_ij[1]]==1:
                Zq = np.random.binomial(1,q)
                if Zq == 0:
                    paysage_tp1[i,j] = 0
                elif Zq == 1: 
                
                        
                


        