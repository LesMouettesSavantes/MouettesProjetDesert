# generateur de décision
import random
import numpy as np
import matplotlib.pyplot as plt

list_decisions = ["Je pars a droite", "je pars a gauche", 'je vais tout droit', "je recule", "je reste sur place"]
N = len(list_decisions)
u = random.randint(0, N-1)
mydecision  = list_decisions[u]
print(mydecision)


#############################
print(range(4))

for i in range(10):
    u = random.randint(0, N-1)
    mydecision  = list_decisions[u]
    print(mydecision)

print('---------------Fin chemin 1-------------')
possible_decisions = ["Je vais vers le nord", "je pars a l'est", 'je vais vers le  sud', "je pars à l'ouest", "je reste sur place"]
print('---------------Début chemin 2-------------')


Nstep = 200
for i in range(1,Nstep):
    u = random.randint(0, N-1)
    mydecision  = list_decisions[u]
    print(mydecision)
 
 
 
pos  = np.zeros( (Nstep, 2) )
mydecision = []
for i in range(1,Nstep):
    u = random.sample(range(N), 1,counts=[2,1,1,1,1])[0]
    mydecision.append(list_decisions[u])
    if (u==0):
        pos[i] = pos[i-1] + (0,1)
    if (u==1):
        pos[i] = pos[i-1] + (1,0)
    if (u==2):
        pos[i] = pos[i-1] + (0,-1)
    if (u==3):
        pos[i] = pos[i-1] + (-1,0)
    if (u==4):
        pos[i] = pos[i-1]
        
print(pos)
print(mydecision)
plt.plot(pos[:,0],pos[:,1],marker = 'o',markersize=4)
plt.title("2D Random Walk")
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
for i, (x, y) in enumerate(zip(pos[:,0],pos[:,1])):
        if i % (1) == 0:  # Annotate every 10% of the steps
            plt.annotate(i, (x, y), textcoords="offset points", xytext=(0,5), ha='center')
    
    
plt.show()

# On veut maintenant marcher aléatoirement dans un champ et ne PAS Sortir du champ. 


print('---------------Début chemin 3-------------')


