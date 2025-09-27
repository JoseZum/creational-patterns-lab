from .ConexionBaseDatos import ConexionBaseDatos

class GestionarInventarios:
    def generarReporte(self):
        db = ConexionBaseDatos.getInstance()
        db.connect()
        data = db.query("SELECT sku, stock FROM inventarios WHERE stock < 10")
        print("[Inventarios] Reporte:", data)
