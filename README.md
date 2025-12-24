# 📱 CommCare Data Processor : Nettoyage Automatisé

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![CommCare](https://img.shields.io/badge/Data_Source-CommCare-purple?style=for-the-badge)
![Pandas](https://img.shields.io/badge/Library-Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

## 📋 La Problématique
Les exportations de données depuis la plateforme **CommCare** présentent souvent des défis structurels pour l'analyse directe :
1.  **Noms de colonnes techniques :** Présence de préfixes système (ex: `form ...`, `case ...`).
2.  **Typage mixte :** Les champs numériques (prix, quantités) sont souvent exportés comme du texte.
3.  **Formatage :** Espaces multiples et caractères spéciaux dans les en-têtes.

## 🛠️ La Solution (`clean_inscription.py`)

Ce script Python ingère le fichier brut et produit un dataset "Business Ready".

### Transformations appliquées :
* **Standardisation des En-têtes :**
  * Suppression automatique des espaces doubles.
  * Conversion en `snake_case` (minuscules + underscores) pour compatibilité SQL.
  * *Exemple :* `"Montant restant  inscription"` ➡️ `montant_restant_inscription`.

* **Correction des Types (Type Casting) :**
  * Détection et conversion des colonnes Prix/Montants en entiers (`Int`).
  * Gestion des valeurs manquantes (`NaN` -> `0`).

* **Validation GPS :**
  * Vérification de l'intégrité des colonnes Latitude/Longitude pour l'import SIG.

* **Enrichissement (Feature Engineering) :**
  * Calcul automatique du `% Payé` basé sur le prix du paquet et le montant versé.

## 🚀 Utilisation
```bash
pip install pandas
python clean_inscription.py
