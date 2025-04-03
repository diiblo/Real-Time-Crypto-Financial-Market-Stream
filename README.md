# 📊 Real-Time Crypto & Financial Market Stream with Kafka, Spark & PostgreSQL

🚀 **Projet Big Data** visant à construire un pipeline de traitement en temps réel des données financières (cryptomonnaies & marchés boursiers) à l'aide de Kafka, Spark Streaming et PostgreSQL. Le projet inclut également la visualisation des résultats dans Power BI.

---

## 🎯 Objectif pédagogique

Comprendre **comment capter, transformer et analyser** des flux de données financières *en temps réel*, tout en pratiquant l’intégration d’API externes (CryptoCompare & Alpha Vantage) avec les technologies Big Data modernes. Ce projet te prépare à des cas concrets du monde professionnel en data engineering & streaming.

---

## ⚙️ Stack Technique

- **Kafka + Zookeeper** : ingestion des flux en temps réel
- **Spark Structured Streaming** : traitement continu des messages Kafka
- **PostgreSQL** : stockage des données transformées
- **Docker** : containerisation du cluster (Kafka, Spark, Postgres)
- **Power BI** : visualisation en temps réel des données financières
- **APIs** :
  - [CryptoCompare](https://developers.coindesk.com/) – pour les données crypto
  - [Alpha Vantage](https://www.alphavantage.co/) – pour les données boursières

---

## 🧱 Étapes principales

1. **Mise en place du cluster Dockerisé**
   - Réseau dédié `pyspark-cluster`
   - Conteneurs : Kafka, Zookeeper, Spark master/worker, PostgreSQL

2. **Simulation de flux via les APIs publiques**
   - Un script interroge CryptoCompare & Alpha Vantage régulièrement
   - Les données sont envoyées dans un `topic Kafka`

3. **Traitement avec Spark Structured Streaming**
   - Nettoyage, enrichissement & agrégation des données crypto/finance
   - Calcul d’indicateurs financiers (moyenne, delta, tendance)

4. **Stockage dans PostgreSQL**
   - Données transformées injectées via JDBC
   - Tables dédiées : `crypto_data_enriched`, `stock_data_enriched`

5. **Visualisation avec Power BI**
   - Connexion DirectQuery à PostgreSQL
   - Dashboard en temps réel : prix, tendances, volumes

---

## ✅ Objectifs pédagogiques atteints

- Maîtrise de la chaîne ingestion → traitement → stockage → visualisation
- Mise en place d’un environnement Big Data complet avec Docker
- Utilisation de **Spark Streaming avec Kafka**
- Intégration d’**APIs publiques** dans un pipeline temps réel
- Requête SQL & Power BI pour l’analyse métier

---

## 👨‍💻 Auteur

**Moctarr Basiru King Rahman**  
Étudiant Mastère Data Engineering – ECE Paris  
[LinkedIn](https://www.linkedin.com/in/moctarr) | [Email](mailto:moctarrbasiru.kingrahman@edu.ece.fr)

---

## 📄 Licence

Ce projet est sous licence MIT.
