# 🔧 Liste Réparations Backend

API REST Flask pour la gestion des interventions sur machines à café et moulins à café.
Permet de scanner des fiches de réparation (OCR), d'enregistrer les interventions
et de consulter l'historique par numéro de série.

---

## 🚀 Fonctionnalités

- 📷 **Scan OCR** de fiches de réparation manuscrites (EasyOCR)
- 🔧 **Enregistrement** des interventions avec les pièces changées
- 🔍 **Recherche** de l'historique par numéro de série
- 📊 **Statistiques** globales (réparations, machines, pièces)
- 🗄️ **Base de données** SQLite avec migrations Alembic

---

## 🏗️ Architecture
liste_reparations_backend/

├── app.py ← Factory pattern (create_app)
├── config.py ← Config Dev / Prod / Test
├── extensions.py ← SQLAlchemy, Migrate, CORS, Marshmallow
├── requirements.txt
│
├── models/ ← Modèles SQLAlchemy
│ ├── reparation.py ← Entête intervention
│ └── piece_changee.py ← Pièces changées (relation 1→N)
│
├── schemas/ ← Validation & sérialisation Marshmallow
│ ├── reparation_schema.py
│ └── piece_schema.py
│
├── services/ ← Logique métier
│ ├── ocr_service.py ← Analyse OCR des fiches
│ ├── reparation_service.py
│ └── piece_service.py
│
├── controllers/ ← Routes Flask (Blueprints)
│ ├── ocr_controller.py
│ ├── reparation_controller.py
│ └── stats_controller.py
│
└── utils/
└── image_utils.py ← Prétraitement image OpenCV

text

---

## ⚙️ Installation

### Prérequis

- Python 3.13+
- Ubuntu 22.04+ / Debian

### 1. Cloner le projet

```bash
git clone https://github.com/ludo35300/liste_reparations_backend.git
cd liste_reparations_backend
```

### 2. Créer et activer le venv

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Initialiser la base de données

```bash
flask --app app db upgrade
```

### 5. Lancer le serveur

```bash
python3 app.py
```

Le serveur démarre sur **http://localhost:5000**

---

## 📡 Endpoints API

| Méthode | Route | Description |
|---|---|---|
| `POST` | `/api/scan` | Analyse OCR d'une fiche (image) |
| `POST` | `/api/reparations` | Enregistre une intervention |
| `GET` | `/api/reparations/<num_serie>` | Historique d'une machine |
| `GET` | `/api/reparations/<id>` | Détail d'une intervention |
| `DELETE` | `/api/reparations/<id>` | Supprime une intervention |
| `GET` | `/api/stats` | Statistiques globales |

---

## 🧪 Exemples de requêtes

### Créer une réparation

```bash
curl -X POST http://localhost:5000/api/reparations \
  -H "Content-Type: application/json" \
  -d '{
    "numero_serie": "SANTOS-40AN-001",
    "machine_type": "MOULIN SANTOS 40AN",
    "technicien": "Ludo",
    "date_reparation": "25/03/2026",
    "notes": "Remplacement meules + condensateur",
    "pieces": [
      {"ref_piece": "40609", "designation": "CONDENSATEUR 100MF", "quantite": 1},
      {"ref_piece": "00001B", "designation": "PAIRE DE MEULES", "quantite": 1}
    ]
  }'
```

### Consulter l'historique d'une machine

```bash
curl http://localhost:5000/api/reparations/SANTOS-40AN-001
```

### Scanner une fiche

```bash
curl -X POST http://localhost:5000/api/scan \
  -F "image=@/chemin/vers/fiche.jpg"
```

### Statistiques

```bash
curl http://localhost:5000/api/stats
```

---

## 🛠️ Stack technique

| Composant | Technologie |
|---|---|
| Framework | Flask 3.1 |
| ORM | SQLAlchemy 2.0 + Flask-SQLAlchemy |
| Migrations | Flask-Migrate (Alembic) |
| Sérialisation | Marshmallow 4 |
| OCR | EasyOCR 1.7 |
| Vision | OpenCV 4.13 |
| Base de données | SQLite (dev) / PostgreSQL (prod) |

---

## 🔮 Évolutions prévues

- [ ] Frontend Angular
- [ ] Export CSV de l'historique
- [ ] Page de statistiques avec graphiques
- [ ] Support multi-modèles de fiches
- [ ] Authentification JWT
- [ ] Migration PostgreSQL en production

---

## 👤 Auteur

**Ludo35300** 

---

## 📄 Licence

Projet privé — tous droits réservés.