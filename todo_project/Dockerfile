# Utilisation de l'image Python officielle
FROM python:3.10

# Définition du répertoire de travail dans le conteneur
WORKDIR /app

# Copie des fichiers du projet dans le conteneur
COPY . /app/

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port 8000 (port par défaut de Django)
EXPOSE 8000

# Commande pour lancer le serveur Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
