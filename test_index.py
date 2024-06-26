# Définition des documents
docA = "Le petit chat dort"
docB = "Le chat dort"
docC = "Jean dort"
# docD = "peut"

# Création du corpus
corpus = {
    "docA": docA,
    "docB": docB,
    "docC": docC,
    # "docD": docD
}

# Découpage du texte en mots
def decouper_mots(texte):
    return texte.split()

# Initialisation de l'index
index = {}

# Construction de l'index
for doc_id, texte in corpus.items():
    mots = decouper_mots(texte)
    for mot in mots:
        if mot not in index:
            index[mot] = set()
        index[mot].add(doc_id)

# Affichage de l'index
print(f'[INFO-INDEX] : {index}')

# Résultat attendu :
# {'Le': {'docA', 'docB'}, 'petit': {'docA'}, 'chat': {'docA', 'docB'}, 'dort': {'docA', 'docB', 'docC'}, 'Jean': {'docC'}}
