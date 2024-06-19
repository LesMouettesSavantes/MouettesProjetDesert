import random
import matplotlib.pyplot as plt
import numpy as np
import math

# Nombre de pas de la marche aléatoire
num_steps = 1000

# Listes pour stocker les positions x et y
x_positions = [0]
y_positions = [0]

# Générer la marche aléatoire
for _ in range(num_steps):
    # Choisir une direction aléatoire
    direction = random.choice(['N', 'S', 'E', 'W','Stop'])
    dist  = random.uniform(4,10)
    if direction == 'N':  # Nord
        x_positions.append(x_positions[-1])
        y_positions.append(y_positions[-1] + dist)
    elif direction == 'S':  # Sud
        x_positions.append(x_positions[-1])
        y_positions.append(y_positions[-1] - dist)
    elif direction == 'E':  # Est
        x_positions.append(x_positions[-1] + dist)
        y_positions.append(y_positions[-1])
    elif direction == 'W':  # Ouest
        x_positions.append(x_positions[-1] - dist)
        y_positions.append(y_positions[-1])
    elif direction == 'Stop':  # Repos
        x_positions.append(x_positions[-1])
        y_positions.append(y_positions[-1])
        

# Tracer la marche aléatoire
#plt.figure(figsize=(10, 10))
#plt.plot(x_positions, y_positions, marker='o', markersize=2, linestyle='-')

# Mettre en évidence le point initial en rouge
#plt.scatter(x_positions[0], y_positions[0], color='red', s=50, label='Point initial')

# Ajouter un titre et des étiquettes
#plt.title("Marche Aléatoire en 2D")
#plt.xlabel("Position X")
#plt.ylabel("Position Y")
#plt.grid(True)
#plt.legend()
#plt.show()


#####################################################################
# Rester dans un rayon de 100km par rapport au point initial 
#####################################################################
# Nombre de pas de la marche aléatoire
num_steps = 1000


# 
eloign_max = 10
# Listes pour stocker les positions x et y
x_positions = [0]
y_positions = [0]

# Générer la marche aléatoire
for _ in range(num_steps):
    
   
    gen = True
    while gen:
        direction = random.choice(['N', 'S', 'E', 'W','Stop'])  # Choisir une direction aléatoire
        dist  = random.uniform(4,10) # choisir une distance parcourue aléatoire
        # calculer les nouvelles positions
        if direction == 'N':  # Nord
            new_x = x_positions[-1] 
            new_y = y_positions[-1] + dist
        elif direction == 'S':  # Sud
            new_x = x_positions[-1]
            new_y = y_positions[-1] - dist
        elif direction == 'E':  # Est
            new_x = x_positions[-1] + dist
            new_y = y_positions[-1]
        elif direction == 'W':  # Ouest
            new_x = x_positions[-1] - dist
            new_y = y_positions[-1]     
        elif direction == 'Stop':  # Repos
            new_x = x_positions[-1]
            new_y = y_positions[-1]
        eloign = math.sqrt((new_x)**2 + (new_y)**2) # calculer mon éloigenement par rapport à mon point de départ
        if eloign <= eloign_max:
            gen = False
            
    x_positions.append(new_x)
    y_positions.append(new_y)
            

# Tracer la marche aléatoire
plt.figure(figsize=(10, 10))
plt.plot(x_positions, y_positions, marker='o', markersize=3, linestyle='-')

# Mettre en évidence le point initial en rouge
plt.scatter(x_positions[0], y_positions[0], color='red', s=50, label='Point initial')

# Tracer le cercle 
circle = plt.Circle((0, 0), radius=eloign_max , color='r', fill=False, linestyle='--')
plt.gca().add_patch(circle)
    
# Ajouter un titre et des étiquettes
plt.title("Marche Aléatoire contrainte en 2D")
plt.xlabel("Position X")
plt.ylabel("Position Y")
plt.grid(True)
plt.legend()
plt.show()