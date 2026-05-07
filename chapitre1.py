from pulp import *

# 1. Création du problème (Maximisation)
prob1 = LpProblem("Maximisation_Prospects_Simple", LpMaximize)

# 2. Variables de décision (x = Instagram, y = Radio)
# Elles sont continues (ou Integer si vous voulez des nombres entiers de posts)
x = LpVariable("Instagram", lowBound=0, cat='Continuous')
y = LpVariable("Radio", lowBound=0, cat='Continuous')

# 3. Fonction Objectif (Page 5 : Z = 40x + 80y)
prob1 += 40 * x + 80 * y, "Nombre_Total_de_Prospects"

# 4. Contraintes
prob1 += 200 * x + 1000 * y <= 10000, "Budget"
prob1 += 1 * x + 2 * y <= 40, "Temps"
prob1 += x + y <= 30, "Volume_Actions"

# 5. Résolution
prob1.solve()

# 6. Affichage des résultats
print("--- RÉSULTATS CHAPITRE 1 ---")
print(f"Statut : {LpStatus[prob1.status]}")
print(f"Nombre de posts Instagram (x) : {round(x.varValue, 2)}")
print(f"Nombre de spots Radio (y) : {round(y.varValue, 2)}")
print(f"Nombre maximal de prospects (Z) : {round(value(prob1.objective), 2)}")