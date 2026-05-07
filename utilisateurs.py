from pulp import *


print("--- CONFIGURATION DE LA CAMPAGNE PUBLICITAIRE ---")

impact_instagram = float(input("Nombre de prospects par post Instagram (ex: 40) : "))
impact_radio = float(input("Nombre de prospects par spot Radio (ex: 80) : "))
impact_panneaux = float(input("Nombre de prospects par Panneau publicitaire (ex: 60) : "))

cout_unitaire_instagram = float(input("Coût d'un post Instagram (ex: 200) : "))
cout_unitaire_radio = float(input("Coût d'un spot Radio (ex: 1000) : "))
cout_unitaire_panneaux = float(input("Coût d'un Panneau (ex: 500) : "))
budget_total_disponible = float(input("Budget TOTAL alloué par l'université (ex: 10000) : "))

temps_unitaire_instagram = float(input("Heures de travail pour 1 Instagram (ex: 1) : "))
temps_unitaire_radio = float(input("Heures de travail pour 1 Radio (ex: 2) : "))
temps_unitaire_panneaux = float(input("Heures de travail pour 1 Panneau (ex: 3) : "))
temps_total_disponible = float(input("Temps TOTAL disponible en heures (ex: 40) : "))

limite_volume_actions = float(input("Nombre maximum d'actions totales (ex: 30) : "))


mon_probleme = LpProblem("Maximisation_Prospects_Université", LpMaximize)

x = LpVariable("Nombre_Instagram", lowBound=0, cat='Continuous')
y = LpVariable("Nombre_Radio", lowBound=0, cat='Continuous')
w = LpVariable("Nombre_Panneaux", lowBound=0, cat='Continuous')

mon_probleme += (impact_instagram * x) + (impact_radio * y) + (impact_panneaux * w)

mon_probleme += (cout_unitaire_instagram * x) + (cout_unitaire_radio * y) + (cout_unitaire_panneaux * w) <= budget_total_disponible, "Contrainte_Budget"


mon_probleme += (temps_unitaire_instagram * x) + (temps_unitaire_radio * y) + (temps_unitaire_panneaux * w) <= temps_total_disponible, "Contrainte_Temps"

mon_probleme += x + y + w <= limite_volume_actions, "Contrainte_Volume"



print("\nCalcul de la solution optimale en cours...")
mon_probleme.solve()

print("\n" + "="*40)
print("       RÉSULTATS DE L'OPTIMISATION")
print("="*40)
print(f"Statut de la solution : {LpStatus[mon_probleme.status]}")

print(f"\nACTIONS À RÉALISER :")
print(f"- Posts Instagram : {round(x.varValue, 3)}")
print(f"- Spots Radio     : {round(y.varValue, 3)}")
print(f"- Panneaux        : {round(w.varValue, 3)}")

print(f"\nSCORE FINAL :")
print(f"Nombre maximum de prospects : {round(value(mon_probleme.objective), 2)}")
print("="*40)
