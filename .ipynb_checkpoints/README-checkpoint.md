# 📊 Real-Time Crypto & Financial Market Stream with Kafka, Spark & PostgreSQL

🚀 Projet Big Data complet simulant un pipeline temps réel de données financières (cryptomonnaies & marchés boursiers) avec ingestion Kafka, traitement Spark, stockage PostgreSQL et visualisation Power BI.

---

## 🎯 Objectif pédagogique

Comprendre et mettre en œuvre un **pipeline de streaming temps réel** basé sur :
- Ingestion de flux API (crypto & actions)
- Traitement distribué avec Spark Structured Streaming
- Stockage structuré dans PostgreSQL
- Visualisation métier dans Power BI

🎓 Ce projet s’inspire des cas concrets rencontrés en entreprise pour te préparer au monde professionnel (Data Engineering / Streaming).

---

## ⚙️ Stack Technique

| Composant             | Rôle                                       |
|----------------------|--------------------------------------------|
| **Kafka / Zookeeper**| Ingestion de flux temps réel               |
| **Spark Streaming**  | Traitement des flux Kafka                  |
| **PostgreSQL**       | Stockage des données transformées          |
| **Docker**           | Containerisation du cluster Big Data       |
| **Power BI**         | Dashboard de visualisation en temps réel   |
| **APIs utilisées**   | CryptoCompare (crypto), Finnhub (actions)  |

---

## 🧱 Architecture du Projet

```
producers/       # Scripts producteurs Kafka (API → Kafka)
consumers/       # Scripts consommateurs Kafka (Kafka → PostgreSQL)
utils/           # Fichiers utilitaires (connexion DB, Kafka)
notebooks/       # Analyse exploratoire & traitement Spark
docs/            # Étapes, configurations et documentation
.env             # Variables d'environnement (non versionné)
start_pipeline.bat  # Script de lancement automatique (Windows)
```

---

## 🚀 Pipeline Étape par Étape

1. **🧱 Mise en place du cluster Dockerisé**
   - Réseau dédié `spark-cluster`
   - Services : Kafka, Zookeeper, Spark master/worker, PostgreSQL

2. **🔌 Ingestion de données via API**
   - `producer_crypto.py` interroge CryptoCompare (BTC, ETH…)
   - `producer_stocks.py` interroge Finnhub (AAPL, MSFT…)
   - Les données sont envoyées dans `crypto_topic` et `stock_topic`

3. **🔥 Traitement Spark Streaming**
   - Lecture temps réel des topics Kafka
   - Parsing JSON, transformation & agrégation

4. **🗄 Stockage dans PostgreSQL**
   - Connexion via JDBC
   - Tables `crypto_data` et `stock_data` alimentées en direct

5. **📈 Visualisation avec Power BI**
   - Connexion DirectQuery à PostgreSQL
   - Dashboard : prix, volumes, tendances

---

## 📦 Bonnes pratiques

- Variables sensibles gérées via `.env` et `python-dotenv`
- Scripts réutilisables et modulaires (`db_utils.py`, `kafka_utils.py`)
- Lancement automatisé avec `start_pipeline.bat`
- Projet structuré par rôle : ingestion, traitement, stockage, visualisation

---

## ✅ Compétences mises en pratique

- 📌 Spark Structured Streaming
- 📌 Kafka Topics & Producers/Consumers Python
- 📌 Connexion Python ↔ PostgreSQL
- 📌 Containerisation Big Data avec Docker
- 📌 Requêtage SQL pour Power BI

---

## 👨‍💻 Auteur

**Moctarr Basiru King Rahman**  
🎓 Étudiant Mastère Data Engineering – ECE Paris  
🔗 [LinkedIn](https://www.linkedin.com/in/moctarr)  
📧 [Email](mailto:moctarrbasiru.kingrahman@edu.ece.fr)

---

## 📄 Licence

MIT License – libre réutilisation pour but pédagogique et démonstratif.