import pandas as pd
import os

# --- CONFIGURATION ---
# Chemin du dossier (basé sur votre demande)
# Note : Pour que cela marche sur votre PC, assurez-vous que le fichier est bien dans ce dossier
FOLDER_PATH = r"C:\Users\HP\OneDrive\Bureau\Data generated with python\Main file"
INPUT_FILE = "Inscription - Inscription (1).csv"
OUTPUT_FILE = "cleaned_inscription_ready.csv"

def clean_inscription_data():
    full_input_path = os.path.join(FOLDER_PATH, INPUT_FILE)
    full_output_path = os.path.join(FOLDER_PATH, OUTPUT_FILE)

    print(f"🔄 Chargement du fichier : {full_input_path}")

    try:
        # On essaie de charger le fichier
        # Si le fichier n'est pas au bon endroit, on teste le dossier courant (pour VS Code)
        if not os.path.exists(full_input_path):
            print(f"⚠️ Fichier introuvable dans le dossier spécifié. Tentative dans le dossier local...")
            full_input_path = INPUT_FILE
            full_output_path = OUTPUT_FILE
        
        df = pd.read_csv(full_input_path)
    except FileNotFoundError:
        print("❌ Erreur critique : Impossible de trouver le fichier CSV.")
        return

    # 1. Nettoyage des Noms de Colonnes
    # Ex: "Point focal" -> "point_focal", "Montant restant  inscription" -> "montant_restant_inscription"
    df.columns = (df.columns
                  .str.strip()
                  .str.lower()
                  .str.replace('  ', ' ') # Double espace
                  .str.replace(' ', '_')
                  .str.replace('é', 'e')
                  .str.replace('è', 'e')
    )
    print("✅ Colonnes standardisées.")

    # 2. Nettoyage des Prix (Problème fréquent : texte au lieu de nombre)
    # On force la conversion en numérique pour 'prix_du_paquet'
    if 'prix_du_paquet' in df.columns:
        df['prix_du_paquet'] = pd.to_numeric(df['prix_du_paquet'], errors='coerce').fillna(0).astype(int)

    # 3. Validation des Dates
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # 4. Vérification GPS
    # Le fichier semble déjà avoir Latitude/Longitude, on s'assure qu'elles sont propres
    cols_gps = ['latitude', 'longitude']
    for col in cols_gps:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # 5. Feature Engineering (Optionnel mais utile)
    # Calcul du % payé
    if 'montant_paye_inscription' in df.columns and 'prix_du_paquet' in df.columns:
        df['pourcentage_paye'] = df.apply(
            lambda x: round((x['montant_paye_inscription'] / x['prix_du_paquet'] * 100), 1) 
            if x['prix_du_paquet'] > 0 else 0, axis=1
        )

    # 6. Exportation
    df.to_csv(full_output_path, index=False)
    print(f"💾 Fichier nettoyé sauvegardé sous : {full_output_path}")
    
    # Petit aperçu
    print("\n--- Aperçu des données nettoyées ---")
    print(df[['point_focal', 'village', 'prix_du_paquet', 'latitude', 'longitude']].head())

if __name__ == "__main__":
    clean_inscription_data()