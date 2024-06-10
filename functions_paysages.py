import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

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
    plt.figure(figsize=(6, 6))
    plt.title(title)
    
    # Création de la heatmap
    ax  = sns.heatmap(-paysage, cbar=False, cmap='gray', linecolor='black', linewidths=0.5, annot=False, fmt="d", xticklabels=False, yticklabels=False)
    for _, spine in ax.spines.items():
        spine.set_visible(True)
        spine.set_color('black')
        spine.set_linewidth(1.5)
    # Affichage de la carte thermique
    plt.show()


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
def get_von_neumann_neighbors(n, i,j):
    neighbors = []

    neighbor_offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for offset in neighbor_offsets:
        new_row, new_col = i + offset[0], j + offset[1]
        if 0 <= new_row < n and 0 <= new_col < n:
            neighbors.append([new_row, new_col])

    return neighbors

#------------------------------------------------------ 
#def get_von_neumann_neighbors_for_two(n,i,j,iprime,jprime):
    
         
     
