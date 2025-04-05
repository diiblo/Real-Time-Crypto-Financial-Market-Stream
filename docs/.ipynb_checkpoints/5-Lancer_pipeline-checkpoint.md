# 🟢 5. Lancer le Pipeline de Streaming Temps Réel

Une fois l’architecture mise en place (Kafka, Spark, PostgreSQL), cette étape permet de démarrer tout le pipeline (producteurs + consommateurs) et de vérifier que les données circulent bien.

---


## ⚠️ Étape indispensable avant de lancer le pipeline

Avant de lancer les producteurs et consommateurs, tu dois **initialiser Spark** depuis le notebook.

Dans le fichier `notebooks/Notebook.ipynb`, exécute cette cellule pour créer la `SparkSession` :

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("CryptoStockRealTimeProcessing") \
    .master("spark://spark-master:7077") \
    .config("spark.executor.memory", "2g") \
    .config("spark.jars", "/usr/local/spark/jars/postgresql-42.6.0.jar,/usr/local/spark/jars/spark-sql-kafka-0-10_2.12-3.4.0.jar,/usr/local/spark/jars/kafka-clients-2.8.0.jar") \
    .getOrCreate()

print(f"Spark version: {spark.version}")
```
---

## 📦 Contenu du pipeline

- **Producer Crypto** : récupère les prix en temps réel via l'API CryptoCompare → envoie vers `crypto_topic` Kafka
- **Producer Stocks** : récupère les actions via l’API Finnhub → envoie vers `stock_topic`
- **Consumer Crypto** : consomme `crypto_topic` et insère dans PostgreSQL
- **Consumer Stocks** : consomme `stock_topic` et insère dans PostgreSQL

---

## 🚀 Lancement automatique (Windows)

Exécute simplement le script suivant pour tout démarrer :

```bash
start_pipeline.bat
```

Cela ouvrira **quatre fenêtres** :
- `producer_crypto.py`
- `producer_stocks.py`
- `consumer_crypto.py`
- `consumer_stocks.py`

🛑 Pour arrêter : utilise `Ctrl + C` dans chaque fenêtre ou ferme-la manuellement.

---

## 💻 Lancement manuel (depuis un terminal)

Tu peux aussi exécuter manuellement chaque fichier :

```bash
python producers/producer_crypto.py
python producers/producer_stocks.py

# Attendre 5 secondes
python consumers/consumer_crypto.py
python consumers/consumer_stocks.py
```

---

## 🧪 Vérification

- 📬 **Kafka** : Tu verras dans le terminal des messages `envoyés` et `reçus`
- 📊 **PostgreSQL** : Connecte-toi à la base :
```bash
docker exec -it pg-ds-dellstore psql -U postgres -d crypto_finance_db
```

Puis exécute :
```sql
SELECT * FROM crypto_data;
SELECT * FROM stock_data;
```

---

## ⚠️ Pré-requis

- Le fichier `.env` doit exister à la racine avec tes identifiants