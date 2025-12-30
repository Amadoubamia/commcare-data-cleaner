# 📱 CommCare Data Processor : Nettoyage, Analyse Automatisée & Cartographie SIG

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Library-Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Business Intelligence](https://img.shields.io/badge/Analysis-Business_Intelligence-orange?style=for-the-badge)

## 📋 La Problématique
Les données brutes exportées de CommCare nécessitent un traitement rigoureux avant de pouvoir servir à la prise de décision stratégique (erreurs de format, types de données incorrects, etc.).

Ce projet propose une solution complète en deux étapes : **Nettoyage ETL** + **Analyse Business**.

## 🛠️ Module 1 : Nettoyage (`clean_inscription.py`)
Ce script transforme les données brutes en un dataset fiable :
* **Standardisation :** Conversion des en-têtes en `snake_case`.
* **Typage :** Conversion des prix (texte) en entiers pour les calculs.
* **Qualité :** Validation des coordonnées GPS et des dates.

## 📊 Module 2 : Analyse Business (`analyze_data.py`)
Ce script agit comme un tableau de bord automatique, répondant aux questions clés :

| Indicateur (KPI) | Résultat Automatisé (Exemple) |
| :--- | :--- |
| **Total Inscrits** | 261 Producteurs |
| **Volume Financier** | 522 000 FCFA |
| **Top Zone** | TOUKOTO |
| **Inclusion** | 81.2% de Femmes |
| **Best-Seller** | Paquet `dap_special_38000` |


## 🗺️ Module 3 : Cartographie & SIG (`generate_map.py`)

Ce module transforme les données tabulaires en outils visuels pour la gestion territoriale.

### Fonctionnalités :
1.  **Carte Interactive Web :** Génération d'une carte HTML autonome avec `Folium` (librairie basée sur Leaflet.js). Permet de cliquer sur chaque producteur pour voir ses détails (Nom, Village, Paquet).
2.  **Export QGIS :** Création automatique d'un fichier `GeoJSON` standard pour l'intégration dans les Systèmes d'Information Géographique.

### 📸 Aperçu du Résultat
*(Carte générée automatiquement montrant la répartition des producteurs)*

![Carte Interactive](map_preview.jpg)

### 💻 Extrait du Code
```python
# Création de la carte centrée sur la moyenne des points GPS
m = folium.Map(location=[df['latitude'].mean(), df['longitude'].mean()], zoom_start=10)

# Ajout des marqueurs avec Popup
folium.Marker(
    location=[row['latitude'], row['longitude']],
    popup=f"{row['nom_et_prenom']} ({row['village']})",
    icon=folium.Icon(color='green', icon='user')
).add_to(m)
## 🚀 Comment l'utiliser
```bash
# 1. Installer les dépendances
pip install pandas

# 2. Lancer le nettoyage
python clean_inscription.py

# 3. Générer le rapport d'analyse
python analyze_data.py


