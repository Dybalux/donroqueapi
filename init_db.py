# init_db.py
from db import Base, engine
from app.productos.models import Productos
from app.ventas.models import Venta

print("⚠️  ATENCIÓN: Este script borrará TODAS las tablas existentes y las volverá a crear.")

confirmacion = input("¿Estás seguro? (si/no): ").strip().lower()
if confirmacion == "si":
    print("🧹 Borrando tablas existentes...")
    Base.metadata.drop_all(bind=engine)

    print("🛠️  Creando tablas actualizadas...")
    Base.metadata.create_all(bind=engine)

    print("✅ Listo. Base de datos reseteada con éxito.")
else:
    print("🚫 Operación cancelada.")