# Social Commerce Manager — base de données Django

Base de départ pour Django 5.2 + PostgreSQL. Elle contient les modèles multi-boutiques, commandes, stock, paiements/remboursements, livraisons, factures et notifications.

## Installation
1. Copier les dossiers d'applications dans le projet Django.
2. Installer : `pip install "Django>=5.2,<5.3" "psycopg[binary]>=3.2" Pillow reportlab`
3. Ajouter les applications à `INSTALLED_APPS`.
4. Configurer `AUTH_USER_MODEL = "accounts.User"` AVANT la toute première migration.
5. Configurer `DATABASES` pour PostgreSQL.
6. Exécuter :
   `python manage.py makemigrations accounts stores products customers orders inventory payments deliveries invoices notifications`
   `python manage.py migrate`
   `python manage.py check`

## Isolation stricte des boutiques
Chaque donnée commerciale est associée à `store`. Il faut obligatoirement filtrer toutes les requêtes par boutique active, vérifier les appartenances et confirmer que les objets liés (client, produit, commande, paiement, livreur) appartiennent à la même boutique. Ne jamais faire confiance à un `store_id` reçu du navigateur. Les contraintes des modèles ne remplacent pas les vérifications de service. Ajouter des tests d'accès croisé entre deux boutiques. Pour une protection supplémentaire en production, étudier PostgreSQL Row-Level Security.

## Stock
Confirmer une commande via `inventory.services.confirm_order`, après validation serveur de l'appartenance de l'utilisateur à la boutique. Le service utilise une transaction et des verrous pour empêcher les réservations concurrentes. Prévoir des services séparés pour libérer une réservation à l'annulation et décrémenter le stock physique à l'expédition.

## Montants, PDF, WhatsApp
- Montants en `DecimalField`, devise boutique MGA par défaut.
- Les prix des lignes de commande sont des instantanés.
- `Invoice.pdf_file` stocke le chemin du PDF généré avec ReportLab. Générer et stocker les fichiers dans un espace privé.
- `Notification` garde le statut et l'identifiant fournisseur, jamais les jetons secrets.
- L'envoi automatique WhatsApp nécessite une intégration officielle WhatsApp Business Platform/API et les consentements requis; le modèle ne réalise pas l'envoi à lui seul.

## Avant production
Ajouter tests, permissions, transitions métier, journal d'audit, sauvegarde/restauration, stockage sécurisé, gestion des erreurs et migrations testées. Le code fourni est une base de données de départ, pas une application complète.
