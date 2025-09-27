from .ConexionBaseDatos import ConexionBaseDatos

class VentasControlador:
    def actualizarVentas(self):
        db = ConexionBaseDatos.getInstance()
        db.connect()
        data = db.query("INSERT INTO ventas(fecha, total) VALUES (CURRENT_DATE, 100.000)")
        print("[Ventas] Registrado:", data)


