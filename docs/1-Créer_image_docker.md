# Créer une image docker...

---

### Étape 1 : Télécharger l'image Jupyter avec Spark
Les images **Jupyter Docker Stacks** incluent différentes configurations. L'image `jupyter/pyspark-notebook` est celle qui contient Jupyter et Spark.

1. **Télécharger l’image Docker :**
   Ouvrez un terminal et exécutez la commande suivante pour télécharger l’image `jupyter/pyspark-notebook` :
   ```bash
   docker pull jupyter/all-spark-notebook

   ```


2. **Vérifiez que l’image est bien téléchargée :**
   Vous pouvez vérifier avec :
   ```bash
   docker images
   ```
   Vous devriez voir `jupyter/all-spark-notebook` dans la liste.

### Étape 2 : Ajouter des plugins ou outils à l'image
Puisque `jupyter/all-spark-notebook` ne contient pas tout nos outils, nous allons les ajouters, par un `Dockerfile`.

**NB :** Certains, ne sont pas importants, mais peuvent servir pour d'autres projets.
Un Dockerfile est déjà fournit dans mon dépôt [us_election_project](https://github.com/diiblo/us_election_project/blob/main/Dockerfile)

1. **Créer un Dockerfile personnalisé :**
   Dans répertoire de votre choix, créez un fichier appelé `Dockerfile` (sans extension) et ajoutez les lignes suivantes :
   ```dockerfile
   # Utiliser l'image de base Jupyter avec Spark
    FROM jupyter/all-spark-notebook
    
    USER root
    
    # Installer des outils système
    RUN apt-get update && apt-get install -y curl git
    
    # Ajouter des connecteurs JDBC (Au choix)
    RUN curl -o /usr/local/spark/jars/postgresql-42.6.0.jar https://jdbc.postgresql.org/download/postgresql-42.6.0.jar && \
       curl -o /usr/local/spark/jars/mysql-connector-java-8.0.34.jar https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.34/mysql-connector-java-8.0.34.jar && \
       curl -o /usr/local/spark/jars/spark-sql-kafka-0-10_2.12-3.4.0.jar https://repo1.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.12/3.4.0/spark-sql-kafka-0-10_2.12-3.4.0.jar && \
       curl -o /usr/local/spark/jars/mongo-spark-connector_2.12-10.2.0.jar https://repo1.maven.org/maven2/org/mongodb/spark/mongo-spark-connector_2.12/10.2.0/mongo-spark-connector_2.12-10.2.0.jar && \
       curl -o /usr/local/spark/jars/hadoop-aws-3.3.6.jar https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.6/hadoop-aws-3.3.6.jar
    
    # Installer des bibliothèques Python
    RUN pip install psycopg2-binary kafka-python python-dotenv
    
    # Changer l’utilisateur par défaut pour Jupyter Notebook
    USER $NB_USER
    
    # Commande par défaut
    CMD ["start-notebook.sh"]
   ```

2. **Construire votre nouvelle image Docker :**
   Dans le terminal, exécutez cette commande pour construire l’image Docker personnalisée (assurez-vous d’être dans le même dossier que le `Dockerfile`) :
   ```bash
   docker build -t datascience-env .
   ```
   Cette commande crée une nouvelle image Docker appelée `datascience-env`

