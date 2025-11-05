# Portfolio Urbain Balogou - Application Django

Application web Django pour gérer et afficher un portfolio professionnel avec des projets, compétences et formations.

## 🎯 Problème résolu

**Avant** : Duplication de code HTML/CSS à chaque nouveau projet
**Après** : Gestion dynamique via une interface admin - plus besoin de dupliquer du code !

## ✨ Fonctionnalités

- 📱 Gestion de projets (applications, sites web, jeux, solutions cloud)
- 🛠️ Gestion des compétences et technologies
- 📚 Gestion des formations
- 📧 Informations de contact centralisées
- 🎨 Interface admin intuitive
- 📊 Analytics (Google Analytics & Tag Manager)
- 🖼️ Upload d'images et vidéos
- 📱 Design responsive

## 🚀 Installation

### Prérequis
- Python 3.8+
- pip

### Étapes d'installation

1. **Installer les dépendances**
```bash
pip install django pillow
```

2. **Appliquer les migrations**
```bash
python manage.py migrate
```

3. **Populer la base de données avec les données initiales**
```bash
python manage.py populate_data
```

4. **Créer un super-utilisateur pour l'admin**
```bash
python manage.py createsuperuser
```
Suivez les instructions pour créer votre compte admin.

5. **Lancer le serveur**
```bash
python manage.py runserver
```

6. **Accéder à l'application**
- Site web : http://127.0.0.1:8000/
- Interface admin : http://127.0.0.1:8000/admin/

## 📂 Structure du projet

```
mon-site-web-/
├── portfolio/                 # Application principale
│   ├── models.py             # Modèles de données (Project, Skill, etc.)
│   ├── views.py              # Vues Django
│   ├── admin.py              # Configuration de l'admin
│   ├── urls.py               # URLs de l'application
│   ├── templates/            # Templates HTML
│   │   └── portfolio/
│   │       ├── base.html     # Template de base
│   │       ├── home.html     # Page d'accueil
│   │       └── project_detail.html  # Détail d'un projet
│   └── management/
│       └── commands/
│           └── populate_data.py  # Script de migration des données
├── portfolio_site/            # Configuration Django
│   ├── settings.py           # Paramètres
│   └── urls.py               # URLs principales
├── static/                    # Fichiers statiques (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
├── media/                     # Fichiers uploadés
│   └── projects/
│       ├── covers/           # Images de couverture
│       ├── screenshots/      # Captures d'écran
│       └── videos/           # Vidéos de démo
└── manage.py                 # Script de gestion Django
```

## 🎨 Utilisation de l'interface admin

### Ajouter un nouveau projet

1. Connectez-vous à l'admin : http://127.0.0.1:8000/admin/
2. Cliquez sur "Projets" puis "Ajouter projet"
3. Remplissez les informations :
   - Titre et sous-titre
   - Type de projet (Application, Site Web, Cloud, Jeu)
   - Descriptions (courte et complète)
   - Uploadez une image de couverture
   - Sélectionnez les technologies utilisées
   - Ajoutez les fonctionnalités (format JSON : ["feature 1", "feature 2"])
4. Ajoutez des captures d'écran via l'onglet "Screenshots" (inline)
5. Sauvegardez

**Plus besoin de créer un nouveau fichier HTML !** Tout est géré via l'admin.

### Gérer les compétences

1. Allez dans "Compétences"
2. Ajoutez/modifiez les compétences
3. Utilisez des icônes Font Awesome (ex: `fa-brands fa-python`)
4. Définissez l'ordre d'affichage

### Gérer les technologies

1. Allez dans "Technologies"
2. Ajoutez des technologies avec :
   - Nom
   - Icône Font Awesome
   - Couleur (code hex)

### Modifier les informations de contact

1. Allez dans "Informations de contact"
2. Modifiez l'email, téléphone, réseaux sociaux
3. Configurez les IDs Analytics si nécessaire

## 📊 Modèles de données

### Project
- Titre, sous-titre, slug
- Type (application, web, cloud, game)
- Descriptions courte et complète
- Images (couverture, header) et vidéo
- Technologies (ManyToMany)
- Fonctionnalités (JSON)
- Ordre d'affichage

### Screenshot
- Image
- Légende
- Ordre
- Lié à un projet

### Skill
- Nom
- Icône Font Awesome
- Ordre

### Technology
- Nom
- Icône
- Couleur

### Formation
- Titre
- Description
- Durée
- Icône
- Active/Inactive

### ContactInfo (Singleton)
- Email, téléphone, WhatsApp
- Réseaux sociaux
- Analytics IDs

## 🔧 Commandes Django utiles

```bash
# Créer de nouvelles migrations
python manage.py makemigrations

# Appliquer les migrations
python manage.py migrate

# Re-populer la base de données
python manage.py populate_data

# Créer un super-utilisateur
python manage.py createsuperuser

# Lancer le serveur
python manage.py runserver

# Lancer le shell Django
python manage.py shell
```

## 🎯 Avantages par rapport à l'ancienne version

| Avant (HTML statique) | Après (Django) |
|----------------------|----------------|
| ❌ Code dupliqué dans 8+ fichiers | ✅ Template unique réutilisable |
| ❌ Modification manuelle du HTML pour chaque projet | ✅ Ajout via interface admin en 2 minutes |
| ❌ Images dispersées dans le dossier racine | ✅ Organisation automatique des médias |
| ❌ Risque d'incohérence entre les pages | ✅ Données centralisées dans la base |
| ❌ Pas de recherche/filtrage | ✅ Filtrage par type de projet |
| ❌ Maintenance difficile | ✅ Maintenance simplifiée |

## 📝 Exemple d'ajout de projet

**Avant (HTML statique)** :
1. Copier portfolio-template.html
2. Renommer en portfolio-nouveau-projet.html
3. Modifier tout le HTML (titre, description, images...)
4. Copier/coller le CSS (500+ lignes)
5. Modifier index.html pour ajouter le lien
6. Uploader les images manuellement
7. Tester sur tous les navigateurs

**Maintenant (Django)** :
1. Aller dans l'admin
2. Cliquer sur "Ajouter projet"
3. Remplir le formulaire
4. Upload les images
5. Sauvegarder
6. **C'est tout ! Le projet apparaît automatiquement sur le site**

## 🤝 Contribution

Pour ajouter de nouvelles fonctionnalités :
1. Modifier les modèles dans `portfolio/models.py`
2. Créer les migrations : `python manage.py makemigrations`
3. Appliquer : `python manage.py migrate`
4. Mettre à jour l'admin dans `portfolio/admin.py`
5. Mettre à jour les templates si nécessaire

## 📧 Contact

- **Email** : urbainbalogou19@gmail.com
- **Téléphone** : +228 70 43 60 43

## 📄 Licence

Ce projet est privé et appartient à Urbain Balogou.
