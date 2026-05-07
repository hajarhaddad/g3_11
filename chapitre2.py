from pulp import *

# 1. Création du problème
prob2 = LpProblem("Maximisation_Prospects_Complexe", LpMaximize)

# 2. Variables de décision
x = LpVariable("Instagram", lowBound=0)
y = LpVariable("Radio", lowBound=0)
w = LpVariable("Panneaux", lowBound=0)

# 3. Fonction Objectif (Page 9 : P = 40x + 80y + 60w)
prob2 += 40 * x + 80 * y + 60 * w, "Prospects_Totaux"

# 4. Contraintes
prob2 += 200 * x + 1000 * y + 500 * w <= 10000, "Budget"
prob2 += 1 * x + 2 * y + 3 * w <= 40, "Temps"
prob2 += x + y + w <= 30, "Volume"

# 5. Résolution
prob2.solve()

# 6. Affichage
print("\n--- RÉSULTATS CHAPITRE 2 (Simplex) ---")
print(f"Instagram (x) : {round(x.varValue, 4)}")
print(f"Radio (y) : {round(y.varValue, 4)}")
print(f"Panneaux (w) : {round(w.varValue, 4)}")
print(f"Valeur optimale de P (Prospects) : {round(value(prob2.objective), 3)}")