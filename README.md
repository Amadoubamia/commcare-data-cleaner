# 📱 CommCare Data Processor : Nettoyage & Analyse Automatisée

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

## 🚀 Comment l'utiliser
```bash
# 1. Installer les dépendances
pip install pandas

# 2. Lancer le nettoyage
python clean_inscription.py

# 3. Générer le rapport d'analyse
python analyze_data.py
