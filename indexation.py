import glob
import json
import os

# ----------------------------------Définition des fonctions------------------------ #
def lire_fichier(chemin):
    with open(chemin, 'r', encoding='utf-8') as fichier:
        return fichier.read()

# ----------------------------------Découpade des mots------------------------ #
def decouper_mots(texte):
    return texte.split()

# ----------------------------------Ajouts des mots------------------------ #
def ajouter_mot_a_index(mot, chemin, index):
    if mot not in index:
        index[mot] = set()
    index[mot].add(chemin)

# ----------------------------------Construction des index------------------------ #
def construire_index(chemin_pattern, index):
    for chemin in glob.glob(chemin_pattern)[:5]:
        chaine = lire_fichier(chemin)
        mots = decouper_mots(chaine)
        for mot in mots:
            ajouter_mot_a_index(mot, chemin, index)

# ----------------------------------Affichage des information des indexes------------------------ #
def afficher_infos_index(index):
    print("Taille du vocabulaire :", len(index))
    print("Échantillon du vocabulaire :", list(index.keys())[:50])

# ----------------------------------Chemin des documents------------------------ #
def afficher_documents_mots(mots_interessants, index):
    for mot in mots_interessants:
        print(f"Documents contenant '{mot}':", index.get(mot, f"Le mot '{mot}' n'est pas dans l'index."))

# ----------------------------------Conversion en JSON------------------------ #
def serialiser_index(index, nom_fichier):
    dossier_destination = "output"
    chemin_complet = os.path.join(dossier_destination, nom_fichier)
    
    # Vérification de l'existance du dossier 'output'
    if not os.path.exists(dossier_destination):
        os.makedirs(dossier_destination)
    
    # Conversion des ensembles en listes pour la sérialisation JSON
    index_serializable = {mot: list(liste_fichiers) for mot, liste_fichiers in index.items()}
    
    # Stockage de l'index au format JSON
    with open(chemin_complet, "w", encoding='utf-8') as fichier_json:
        fichier_json.write(json.dumps(index_serializable, ensure_ascii=False, indent=4))
    
    print(f"Index stocké dans '{chemin_complet}'.")

# Utilisation des fonctions
index = {}
construire_index("./dataset/fr/*", index)
afficher_infos_index(index)
afficher_documents_mots(["indique", "européenne", "toto"], index)
serialiser_index(index, "index.json")