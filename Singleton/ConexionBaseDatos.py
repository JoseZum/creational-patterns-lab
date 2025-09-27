class ConexionBaseDatos:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connected = False
        return cls._instance

    @classmethod
    def getInstance(cls):
        return cls()

    def connect(self):
        if not self.connected:
            self.connected = True
            print("Base de datos conectada")

    def disconnect(self):
        if self.connected:
            self.connected = False
            print("Base de datos desconectada")

    def query(self, query):
        if not self.connected:
            raise RuntimeError("Debe conectarse primero con connect()")
        print(f"[DB] Ejecutando: {query}")
        return {"ok": True, "query": query}
