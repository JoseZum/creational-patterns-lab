from .ConexionBaseDatos  import ConexionBaseDatos

class ReportesFinancieros:
    def actualizarInventario(self):
        db = ConexionBaseDatos.getInstance()
        db.connect()
        data = db.query("UPDATE inventarios SET reservado = reservado + 5 WHERE sku='retail-123'")
        print("[Finanzas] Ajuste:", data)
