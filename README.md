# Social Commerce Manager

**Application web de gestion commerciale et de suivi des commandes pour les vendeurs sur Facebook et WhatsApp.**

<p align="center">
  <strong>Gérez vos clients, vos produits, vos commandes et vos livraisons depuis une seule plateforme.</strong>
</p>

---

## 1. Présentation du projet

**Social Commerce Manager** est une application web conçue pour faciliter la gestion des activités commerciales des vendeurs qui utilisent les réseaux sociaux, notamment Facebook et WhatsApp, pour vendre leurs produits.

L'application centralise les principales opérations commerciales dans une plateforme unique : gestion des clients, produits, stocks, commandes, paiements, livraisons et facturation.

Elle adopte une architecture **multi-vendeurs**, permettant à plusieurs commerçants d'utiliser la même plateforme tout en conservant une séparation stricte de leurs données.

L'objectif principal est de simplifier le travail quotidien des vendeurs, d'améliorer le suivi des commandes et d'optimiser la gestion de leur activité commerciale.

## 2. Objectifs du projet

- Centraliser la gestion des commandes provenant des réseaux sociaux.
- Simplifier l'enregistrement et le suivi des commandes.
- Organiser les informations des clients.
- Assurer un suivi efficace des produits et des stocks.
- Faciliter la gestion des paiements et des livraisons.
- Automatiser certaines tâches commerciales.
- Générer des factures au format PDF.
- Améliorer la communication avec les clients grâce aux notifications WhatsApp.
- Permettre à plusieurs vendeurs de travailler sur une même plateforme sans partager leurs données privées.
- Préparer une évolution vers un modèle économique basé sur des abonnements mensuels.

## 3. Fonctionnalités principales

### 3.1. Gestion des comptes et des vendeurs

- Inscription et authentification des utilisateurs.
- Connexion et déconnexion sécurisées.
- Gestion des profils vendeurs.
- Modification des informations personnelles.
- Gestion des accès et des autorisations.
- Séparation des données entre les différents vendeurs.
- Gestion des comptes utilisateurs.

### 3.2. Gestion des clients

- Enregistrement des nouveaux clients.
- Modification des informations clients.
- Suppression des clients.
- Consultation de la liste des clients.
- Enregistrement des coordonnées téléphoniques.
- Gestion des adresses de livraison.
- Consultation de l'historique des commandes.
- Recherche et filtrage des clients.

### 3.3. Gestion des produits et des stocks

- Ajout de nouveaux produits.
- Modification des informations des produits.
- Suppression des produits.
- Gestion des catégories.
- Enregistrement des prix de vente.
- Gestion des quantités disponibles.
- Suivi des entrées et sorties de stock.
- Alertes de stock faible.
- Historique des mouvements de stock.

**Réservation du stock :**

Le stock est réservé automatiquement lors de la confirmation d'une commande afin d'éviter les ventes dépassant les quantités disponibles.

### 3.4. Gestion des commandes

- Création manuelle des commandes.
- Association des commandes aux clients.
- Ajout de plusieurs produits dans une commande.
- Calcul automatique des montants.
- Gestion des quantités commandées.
- Modification et consultation des commandes.
- Suivi de l'état des commandes.
- Historique des commandes.
- Recherche et filtrage par statut ou par date.

**Statuts des commandes :**

- En attente.
- Confirmée.
- En préparation.
- Expédiée.
- Livrée.
- Annulée.

### 3.5. Gestion des paiements

- Enregistrement des paiements.
- Suivi des paiements effectués.
- Gestion des paiements partiels.
- Calcul automatique des montants restants.
- Consultation de l'historique des transactions.
- Gestion des différents modes de paiement.
- Suivi des commandes payées et non payées.

### 3.6. Gestion des livraisons

- Enregistrement des informations de livraison.
- Association d'une livraison à une commande.
- Gestion des adresses de livraison.
- Attribution des livraisons à un livreur.
- Possibilité pour le vendeur d'effectuer lui-même la livraison.
- Suivi de l'état des livraisons.
- Gestion des frais de livraison.
- Historique des livraisons.

**Statuts des livraisons :**

- En attente.
- En préparation.
- En cours de livraison.
- Livrée.
- Échec de livraison.
- Annulée.

### 3.7. Gestion des factures PDF

- Génération automatique des factures.
- Création de documents PDF.
- Informations sur le vendeur et le client.
- Détail des produits commandés.
- Quantités et prix unitaires.
- Calcul du montant total.
- Affichage des frais de livraison.
- Date et numéro de facture.
- Téléchargement et impression des factures.

### 3.8. Notifications WhatsApp

- Préparation des notifications destinées aux clients.
- Confirmation des commandes.
- Information sur l'état des commandes.
- Notifications concernant les livraisons.
- Communication des informations de paiement.

*L'envoi automatisé nécessite une intégration avec une API ou un service compatible WhatsApp.*

### 3.9. Tableau de bord et statistiques

- Nombre total de commandes.
- Nombre de clients enregistrés.
- Nombre de produits disponibles.
- État général des stocks.
- Chiffre d'affaires.
- Suivi des paiements.
- Commandes en attente.
- Commandes livrées.
- Statistiques des ventes.
- Visualisation des performances commerciales.

### 3.10. Gestion des abonnements

L'application prévoit une possibilité de commercialisation sous forme de service avec abonnement mensuel.

Fonctionnalités envisagées :

- Gestion des abonnements des vendeurs.
- Définition des formules d'abonnement.
- Suivi des dates de début et d'expiration.
- Gestion des renouvellements.
- Suivi des paiements d'abonnement.
- Activation et suspension des abonnements.
- Gestion des fonctionnalités selon la formule choisie.

## 4. Architecture multi-vendeurs

Social Commerce Manager utilise une architecture multi-vendeurs permettant à plusieurs commerçants de partager une même application.

Chaque vendeur dispose de son propre espace de travail.

**Principe de fonctionnement :**

- Un vendeur possède ses propres clients.
- Un vendeur gère ses propres produits.
- Un vendeur consulte uniquement ses commandes.
- Les stocks sont indépendants pour chaque vendeur.
- Les paiements et les livraisons sont associés au vendeur concerné.
- Les données d'un vendeur ne sont pas accessibles aux autres vendeurs.

Cette organisation garantit une meilleure confidentialité et une gestion indépendante des activités commerciales.

## 5. Technologies utilisées

| Technologie | Utilisation |
|---|---|
| Python | Langage de programmation principal |
| Django | Framework de développement backend |
| PostgreSQL | Système de gestion de base de données |
| HTML5 | Structure des pages web |
| CSS3 | Mise en forme et design |
| JavaScript | Interactivité côté client |
| Bootstrap | Framework d'interface responsive |
| ReportLab | Génération des factures PDF |
| WhatsApp API | Intégration des notifications |

## 6. Architecture du projet

Le projet est organisé selon une architecture modulaire Django afin de faciliter la maintenance, l'évolution et la réutilisation du code.

Les principales applications sont :

| Module | Responsabilité |
|---|---|
| accounts | Comptes utilisateurs et authentification |
| customers | Gestion des clients |
| stores | Gestion des vendeurs et des boutiques |
| products | Gestion des produits |
| inventory | Gestion des stocks |
| orders | Gestion des commandes |
| payments | Gestion des paiements |
| deliveries | Gestion des livraisons |
| invoices | Génération des factures PDF |
| notifications | Gestion des notifications |

## 7. Structure du projet

```text
social-commerce-manager/
│
├── README.md
├── manage.py
├── requirements.txt
├── .gitignore
├── .env.example
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── accounts/
├── customers/
├── stores/
├── products/
├── inventory/
├── orders/
├── payments/
├── deliveries/
├── invoices/
├── notifications/
│
├── templates/
├── static/
├── media/
│
└── Les Diagrammes/
    ├── diagramme_cas_utilisation/
    ├── diagramme_classes/
    └── diagramme_sequence/
```

*Cette structure est indicative et doit correspondre à l'organisation réelle du dépôt.*

## 8. Installation et configuration

### 8.1. Prérequis

Avant de commencer, assurez-vous d'avoir installé :

- Python.
- Django.
- PostgreSQL.
- Git.
- Un éditeur de code (Visual Studio Code recommandé).

### 8.2. Cloner le repository

```bash
git clone https://github.com/armailjean/social-commerce-manager.git
```

Accéder au dossier du projet :

```bash
cd social-commerce-manager
```

### 8.3. Créer un environnement virtuel

Sous Windows :

```powershell
python -m venv .venv
```

Activer l'environnement :

```powershell
.venv\Scripts\Activate.ps1
```

### 8.4. Installer les dépendances

```bash
python -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

### 8.5. Configurer PostgreSQL

Créer une base de données PostgreSQL pour le projet.

Exemple :

```sql
CREATE DATABASE social_commerce_db;
```

Configurer ensuite les paramètres de connexion dans le fichier `.env`, notamment :

- DB_NAME
- DB_USER
- DB_PASSWORD
- DB_HOST
- DB_PORT
- SECRET_KEY

Ne jamais publier les véritables mots de passe ou clés secrètes sur GitHub.

### 8.6. Effectuer les migrations

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

### 8.7. Créer un administrateur

```bash
python manage.py createsuperuser
```

### 8.8. Lancer le serveur

```bash
python manage.py runserver
```

Ouvrir ensuite l'application dans le navigateur :

```text
http://127.0.0.1:8000/
```

*Les commandes supposent que le projet Django et ses fichiers de configuration sont correctement configurés.*

## 9. Devise et langues

**Devise principale :** Ariary malgache (MGA).

**Langues de l'interface :**
- Français.
- Malagasy.

L'application est pensée pour répondre aux besoins des vendeurs et commerçants, notamment dans le contexte du commerce en ligne à Madagascar.

## 10. Sécurité et confidentialité

La sécurité constitue un élément important de l'application.

Les principes prévus comprennent :

- Authentification des utilisateurs.
- Protection des données personnelles.
- Gestion des autorisations.
- Isolation des données entre vendeurs.
- Protection contre les accès non autorisés.
- Utilisation des variables d'environnement.
- Protection des informations sensibles.
- Validation des données saisies.

## 11. Perspectives d'évolution

Les évolutions envisagées pour les prochaines versions comprennent :

- Intégration de l'API WhatsApp Business.
- Automatisation de certaines opérations commerciales.
- Amélioration du tableau de bord statistique.
- Intégration de moyens de paiement supplémentaires.
- Développement d'une application mobile.
- Gestion avancée des abonnements.
- Exportation des rapports commerciaux.
- Intégration éventuelle avec Facebook et d'autres plateformes de vente.

## 12. Auteur

**Armail**

Développeur informatique

Compétences :
- Développement Python et Django.
- Développement Java.
- Développement Web.
- Gestion de bases de données.
- PostgreSQL.
- Conception et développement d'applications.

GitHub : [@armailjean](https://github.com/armailjean)

## 13. Licence

Ce projet est destiné à être distribué sous licence MIT, sous réserve de l'ajout du fichier `LICENSE` correspondant et de la confirmation des droits sur les composants utilisés.

---

<p align="center">
  <strong>Social Commerce Manager</strong>
  <br/>
  Simplifier la gestion commerciale. Centraliser les commandes. Développer les ventes.
</p>
