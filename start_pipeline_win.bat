@echo off
title 🚀 Démarrage du pipeline Kafka + Spark + PostgreSQL
echo [INFO] Lancement du pipeline en temps réel...

REM Lancer les producteurs dans des fenêtres distinctes
start cmd /k "python producers\producer_crypto.py"
start cmd /k "python producers\producer_stocks.py"

REM Pause pour que les topics Kafka se remplissent
timeout /t 5 > nul

REM Lancer les consommateurs dans d'autres fenêtres
start cmd /k "python consumers\consumer_crypto.py"
start cmd /k "python consumers\consumer_stocks.py"

echo [OK] Tous les producteurs et consommateurs sont lancés.