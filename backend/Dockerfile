# Utilise l'image de base compatible avec Python 3.13
FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*
# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie le fichier requirements.txt dans le conteneur
COPY req.txt /app/

# Installe les dépendances
RUN pip install --no-cache-dir -r req.txt

# Copie le code de l'application dans le conteneur
COPY . /app/

# Expose le port 8080 pour Django
EXPOSE 8080


# Démarre le serveur de développement Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
# Pour la production, décommentez la ligne suivante et commentez la ligne ci-dessus
# CMD ["gunicorn", "--bind", "0.0.0.0:8080", "config.wsgi:application"]