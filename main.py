from Singleton.Inventarios import GestionarInventarios
from Singleton.Reportes import ReportesFinancieros
from Singleton.Ventas import VentasControlador
from Singleton.ConexionBaseDatos import ConexionBaseDatos


if __name__ == "__main__":

    inv = GestionarInventarios()
    rep = ReportesFinancieros()
    ven = VentasControlador()

    inv.generarReporte()
    rep.actualizarInventario()
    ven.actualizarVentas()

    # Se verifica la misma instancia 
    a = ConexionBaseDatos.getInstance()
    b = ConexionBaseDatos.getInstance()
    print("Misma instancia?", a is b)


