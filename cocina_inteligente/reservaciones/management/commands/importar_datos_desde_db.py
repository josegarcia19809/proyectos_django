from django.core.management.base import BaseCommand
import sqlite3
from reservaciones.models import Cliente, Mesa, Reservacion, Resena


class Command(BaseCommand):
    help = 'Importar datos desde SQLite externa'

    def handle(self, *args, **kwargs):

        # Conectar a la BD externa
        conexion = sqlite3.connect("data/restaurante.db")
        cursor = conexion.cursor()

        self.stdout.write("🚀 Iniciando importación...")

        # ======================
        # 👤 Clientes
        # ======================
        cursor.execute("SELECT id, nombre FROM clientes")
        for id, nombre in cursor.fetchall():
            Cliente.objects.update_or_create(
                id=id,
                defaults={"nombre": nombre}
            )

        # ======================
        # 🪑 Mesas
        # ======================
        cursor.execute("SELECT id, numero_mesa, capacidad FROM mesas")
        for id, numero, capacidad in cursor.fetchall():
            Mesa.objects.update_or_create(
                id=id,
                defaults={
                    "numero_mesa": numero,
                    "capacidad": capacidad
                }
            )

        # ======================
        # 📅 Reservaciones
        # ======================
        cursor.execute("""
        SELECT id, cliente_id, mesa_id, fecha, hora_inicio, hora_fin, numero_personas, estado
        FROM reservaciones
        """)

        for fila in cursor.fetchall():
            Reservacion.objects.update_or_create(
                id=fila[0],
                defaults={
                    "cliente_id": fila[1],
                    "mesa_id": fila[2],
                    "fecha": fila[3],
                    "hora_inicio": fila[4],
                    "hora_fin": fila[5],
                    "numero_personas": fila[6],
                    "estado": fila[7]
                }
            )

        # ======================
        # ⭐ Reseñas
        # ======================
        cursor.execute("SELECT id, cliente_id, calificacion FROM resenas")

        for fila in cursor.fetchall():
            Resena.objects.update_or_create(
                id=fila[0],
                defaults={
                    "cliente_id": fila[1],
                    "calificacion": fila[2]
                }
            )

        # Cerrar conexión
        conexion.close()

        self.stdout.write(self.style.SUCCESS("✅ Importación completada"))