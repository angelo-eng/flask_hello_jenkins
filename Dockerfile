# Dockerfile
FROM python:3.11-slim

# Dépendances système (optionnel si erreurs pip)
RUN apt-get update && apt-get install -y build-essential

# Répertoire de travail
WORKDIR /app

# Copier les fichiers
COPY . /app

# Installer les dépendances
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# Lancer les tests automatiquement
CMD ["python3", "test.py", "-v"]
