# generateur de décision
import random
import numpy as np

list_decisions = ("Je pars a droite", "je pars a gauche", 'je vais tout droit', "je recule", "je reste sur place")
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

list_decisions = ("Je vais vers le nord", "je pars a l'est", 'je vais vers le  sud', "je pars à l'ouest", "je reste sur place")
print('---------------Début chemin 2-------------')

for i in range(20):
    u = random.randint(0, N-1)
    mydecision  = list_decisions[u]
    print(mydecision)
 
pos = np.array([0,0])    
for i in range(20):
    u = random.randint(0, N-1)
    mydecision  = list_decisions[u]
    if (u==0):
        pos = pos + (0,1)
    if (u==1):
        pos = pos + (1,0)
    if (u==2):
        pos = pos + (0,-1)
    if (u==3):
        pos = pos + (-1,0)
    print(pos)