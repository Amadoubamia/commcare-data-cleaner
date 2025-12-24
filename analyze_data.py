import pandas as pd
import os

# Nom du fichier nettoyé (généré à l'étape précédente)
INPUT_FILE = "cleaned_inscription_ready.csv"

def analyze_business_metrics():
    print("--- 📊 RAPPORT D'ANALYSE AUTOMATISÉ ---\n")

    # 1. Importation des données
    try:
        df = pd.read_csv(INPUT_FILE)
    except FileNotFoundError:
        print(f"❌ Erreur : Le fichier '{INPUT_FILE}' est introuvable.")
        print("Veuillez d'abord lancer le script 'clean_inscription.py'.")
        return

    # ---------------------------------------------------------
    # QUESTION 1 : Combien d'inscrits au total ?
    # ---------------------------------------------------------
    total_inscrits = len(df)
    print(f"1️⃣  NOMBRE TOTAL D'INSCRITS :")
    print(f"    -> {total_inscrits} producteurs")
    print("-" * 30)

    # ---------------------------------------------------------
    # QUESTION 2 : Quel est le montant total collecté ?
    # ---------------------------------------------------------
    total_argent = df['montant_paye_inscription'].sum()
    # Astuce : f"{...:,.0f}" permet d'ajouter des espaces pour les milliers
    print(f"2️⃣  MONTANT TOTAL COLLECTÉ :")
    print(f"    -> {total_argent:,.0f} FCFA".replace(",", " "))
    print("-" * 30)

    # ---------------------------------------------------------
    # QUESTION 3 : Quelle zone a collecté le plus d'argent ?
    # ---------------------------------------------------------
    # On groupe les données par 'zone', on somme les montants, et on trie du plus grand au plus petit
    classement_zones = df.groupby('zone')['montant_paye_inscription'].sum().sort_values(ascending=False)
    
    # On prend le premier résultat (le haut du classement)
    meilleure_zone = classement_zones.index[0]
    montant_zone = classement_zones.iloc[0]

    print(f"3️⃣  ZONE LA PLUS PERFORMANTE (Argent) :")
    print(f"    -> {meilleure_zone.upper()} avec {montant_zone:,.0f} FCFA")
    print("-" * 30)

    # ---------------------------------------------------------
    # QUESTION 4 : Quelle est la répartition Hommes/Femmes ?
    # ---------------------------------------------------------
    print(f"4️⃣  RÉPARTITION PAR SEXE :")
    repartition = df['sexe'].value_counts()
    
    # Calcul des pourcentages pour faire plus professionnel
    for sexe, nombre in repartition.items():
        pourcentage = (nombre / total_inscrits) * 100
        print(f"    -> {sexe} : {nombre} personnes ({pourcentage:.1f}%)")
    
    print("\n--- Fin du rapport ---")

if __name__ == "__main__":
    analyze_business_metrics()