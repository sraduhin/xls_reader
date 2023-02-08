import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = 'postgresql://postgres:postgres@db:5432/postgres'
DOCKER_ENV = bool(os.environ.get('DOCKER_ENV', False))
DATABASE_URL = DATABASE_URL if DOCKER_ENV else os.getenv('DATABASE_URL')