import sqlite3

conn = sqlite3.connect('ManipulationDB.db')
cursor = conn.cursor()
print("Connexion à la base de données établie avec succès.")

# Requête SQL pour créer une table 'utilisateurs' 
cursor.execute(''' 
CREATE TABLE IF NOT EXISTS utilisateurs ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nom TEXT NOT NULL, 
    email TEXT UNIQUE NOT NULL 
) 
''')
conn.commit()
print("Table 'utilisateurs' créée avec succès.")

# Données à insérer (avec INSERT OR IGNORE)
donnees_utilisateur = ('Nsengiyumva seraphine', 'nsengiyumvaseraphine123@gmail.com')
cursor.execute("INSERT OR IGNORE INTO utilisateurs (nom, email) VALUES (?, ?)", donnees_utilisateur)
conn.commit()
print("Utilisateur inséré (ou ignoré si déjà existant).")

# Insertion multiple avec protection contre doublons
utilisateurs = [
    ('Seraphine NSENGIYUMVA', 'nsengiyumvaseraphine123@gmail.com'),
    ('Albert Mukunzi', 'albert.mukunzi@gmail.com')
]
cursor.executemany("INSERT OR IGNORE INTO utilisateurs (nom, email) VALUES (?, ?)", utilisateurs)
conn.commit()
print("Utilisateurs insérés (les doublons ont été ignorés).")

#conn.close()
print("Connexion à la base de données fermée.")
# Sélectionner tous les utilisateurs 
cursor.execute("SELECT id, nom, email FROM utilisateurs") 
# Récupérer tous les résultats 
resultats = cursor.fetchall() 
print("Liste de tous les utilisateurs :") 
for utilisateur in resultats: 
    print(utilisateur) 

# Sélectionner un utilisateur en particulier 
nom_recherche = 'Nsengiyumva seraphine' 
cursor.execute("SELECT email FROM utilisateurs WHERE nom=?", 
(nom_recherche,)) 
# Récupérer le premier résultat (ou None si rien n'est trouvé) 
email_trouve = cursor.fetchone() 
print(f"L'e-mail de {nom_recherche} est : {email_trouve[0]}") 

# Mettre à jour l'e-mail de 'Jean Claude Kabayabaya'' 
nouveau_mail = 'nsengiyumvaseraphine123@gmail.com' 
nom_a_modifier = 'Nsengiyumva seraphine' 
cursor.execute("UPDATE utilisateurs SET email=? WHERE nom=?", 
(nouveau_mail, nom_a_modifier)) 
conn.commit() 

conn.close()


