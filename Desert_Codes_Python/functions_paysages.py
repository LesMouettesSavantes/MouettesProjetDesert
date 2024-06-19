import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random


#-------------------------- Toatally random paysage 
def initial_paysage(n,p0): 

    paysage = np.zeros((n, n))
    for i in range(n):
        for j in range (n):
            paysage[i,j]= np.random.binomial(1,p0) 
    return(paysage)      


#------------------------- représentation 
def plot_my_paysage(paysage,title=""):
    # Création de la figure et de l'axe
    fig = plt.figure(figsize=(6, 6))
    plt.title(title)
    
    # Création de la heatmap
    ax  = sns.heatmap(-paysage, cbar=False, cmap='gray', linecolor='black', linewidths=0.5, annot=False, fmt="d", xticklabels=False, yticklabels=False)
    for _, spine in ax.spines.items():
        spine.set_visible(True)
        spine.set_color('black')
        spine.set_linewidth(1.5)
    # Affichage de la carte thermique
    return(fig)


#------------------------------------------------------ 
def get_von_neumann_neighbors(n, i,j):
    neighbors = []

    neighbor_offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for offset in neighbor_offsets:
        new_row, new_col = i + offset[0], j + offset[1]
        if 0 <= new_row < n and 0 <= new_col < n:
            neighbors.append([new_row, new_col])

    return neighbors

#------------------------------------------------------ 
def get_von_neumann_neighbors_2cells(n, i,j,iprime,jprime,paysage = None):
    
    
    if (paysage is None):
        paysage = np.zeros((n,n))
    
    neighbors1 = []
    neighbors2 = []
    neighbor_offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]


    for offset in neighbor_offsets:
        new_row, new_col = i + offset[0], j + offset[1]
        if 0 <= new_row < n and 0 <= new_col < n  and (new_row,new_col) != (iprime,jprime) and paysage[new_row, new_col]==0 :
            neighbors1.append([new_row, new_col])

    for offset in neighbor_offsets:
        new_row, new_col = iprime + offset[0], jprime + offset[1]
        if 0 <= new_row < n and 0 <= new_col < n  and (new_row,new_col) != (i,j) and paysage[new_row, new_col]==0:
            neighbors2.append([new_row, new_col])
            

    return neighbors1+neighbors2

#------------------------------------------------------ 
# transition following Eby model

def transition_EbyModel(paysage_t,n,p,q):

    paysage_tp1 = np.copy(paysage_t)
    
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
                        Vois_ij_Uij  = get_von_neumann_neighbors_2cells(n,i,j,U_ij[0],U_ij[1])  
                        W_ij = random.choice(Vois_ij_Uij)
                        paysage_tp1[W_ij[0],W_ij[1]] = 1 
                    
    return(paysage_tp1)
         
     
