from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
from pathlib import Path
import os

# Cargar .env desde el directorio raíz del proyecto (ajustalo si cambia)
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)
print("🔍 DATABASE_URL:", os.getenv("DATABASE_URL"))

# Obtener y adaptar la URL para SQLAlchemy (CockroachDB se basa en PostgreSQL)
raw_url = os.getenv("DATABASE_URL")
if raw_url is None:
    raise ValueError("No se encontró la variable DATABASE_URL en el entorno.")

# Reemplazamos 'cockroachdb://' por 'postgresql://' para que SQLAlchemy lo entienda
#DATABASE_URL = raw_url.replace("cockroachdb://", "postgresql://")
DATABASE_URL = raw_url

# Crear el motor de conexión
engine = create_engine(DATABASE_URL, echo=False)

# Crear el SessionLocal para usar en los endpoints
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()

# Probar la conexión
try:
    with engine.connect() as conn:
        res = conn.execute(text("SELECT now()")).fetchone()
        print(f"Conexión exitosa a la base de datos: {res[0]}")
except Exception as e:
    print("Error al conectar con la base de datos:")
    print(e)

# Dependencia para usar en los endpoints de FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()