### **Étape 1 : Vérifier si le port 5432 est occupé**
1. **Ouvrez un terminal en mode administrateur** :  
   Appuyez sur `Win + R`, tapez `cmd`, faites un clic droit et sélectionnez **Exécuter en tant qu'administrateur**.

2. Tapez la commande suivante pour vérifier si le port 5432 est utilisé :  
   ```bash
   netstat -ano | findstr :5432
   ```
   Cette commande affiche les informations des connexions utilisant ce port. Les colonnes sont :  
   - **Protocole** (TCP/UDP)  
   - **Adresse locale** (IP et port)  
   - **État de la connexion**  
   - **PID** (Process ID, identifiant du processus).  

   Par exemple, si vous obtenez une ligne comme :  
   ```
   TCP    0.0.0.0:5432    0.0.0.0:0    LISTENING    1234
   ```
   Le **PID (1234)** correspond au processus utilisant le port.

---

### **Étape 2 : Identifier le processus qui occupe le port**
1. Notez le **PID** affiché dans la commande précédente.  
2. Tapez la commande suivante pour identifier le processus :  
   ```bash
   tasklist | findstr 1234
   ```
   Remplacez `1234` par le **PID** obtenu. Cela affiche le nom du programme qui occupe le port.

---

### **Étape 3 : Terminer le processus**
1. Si vous souhaitez libérer le port en arrêtant le processus :  
   ```bash
   taskkill /PID 1234 /F
   ```
   Remplacez `1234` par le **PID** du processus.

2. Vérifiez à nouveau si le port est libéré :  
   ```bash
   netstat -ano | findstr :5432
   ```
   Si aucune ligne ne s'affiche, le port est maintenant libre.

---