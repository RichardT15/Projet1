import math
# Initialisation des variables
F = 10000  # en N
E = 210  # en GPa = 10^3 N/mm^2
L = 100  # en mm

# poutre rectangulaire
b = 10  # en mm
h = 20  # en mm
I_rect = b * (h ** 3) / 12 # Formule de l'inertie de la poutre rectangulaire
# poutre carrée
a = 15  # en mm
I_carr = (a ** 4) / 12 # Formule de l'inertie de la poutre carrée
# poutre ronde
d = 5  # en mm
I_rond = (math.pi) * (d ** 4) / 64 # Formule de l'inertie de la poutre ronde
# poutre creuse
D = 15  # en mm
d = 5  # en mm
I_creu = math.pi * (D ** 4 - d ** 4) / 64 # Formule de l'inertie de la poutre creuse

# Calcul de la section optimale
delta_list = []       # Création d'une liste vide (ne possède aucune valeur)
Inertie = [I_rect , I_carr , I_rond , I_creu] # Création d'une liste des inerties en prenant en compte l'ordre
for I in Inertie:    # Création d'une boucle for pour utiliser chaque élément de la liste Inertie
    delta = F * (L ** 3) / (3 * E * 1000 * I)  # Calcul des différents delta à partir des I de la liste
    delta_list.append(delta) # Insertion des valeurs de delta dans une liste en prenant compte de l'ordre
delta_max = min(delta_list)   # Détermination de la valeur minimale dans la liste

  
if delta_max == delta_list[0]:   # Conditions : si la valeur de delta_max est égale à la première valeur de ans la liste
    section = "rectangulaire"    # La variable section est égale au string "rectangulaire"
elif delta_max == delta_list[1]: # Conditions : si la valeur de delta_max est égale à la deuxième valeur de ans la liste
    section = "carrée"           # La variable section est égale au string "carrée"
elif delta_max == delta_list[2]: # Conditions : si la valeur de delta_max est égale à la troisième valeur de ans la liste
    section = "rond"             # La variable section est égale au string "ronde"
else:                            # Sinon (Puisque la quatrième valeur de la liste est la dernière de la liste)
    section = "creuse"           # La variable section est égale au string "creuse"
print("Le type de section minimisant la déformation maximale est", section + ",","avec un déformation de",'%.2f'%delta_max,"mm")


