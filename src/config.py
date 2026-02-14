"""
Singleton Configuration Loader
Loads global system paths.
"""

class SystemConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SystemConfig, cls).__new__(cls)
            cls._instance.inventory_file = "data/inventory.json"
            cls._instance.map_file = "data/map_data.csv"
            print("[System] Configuration Loaded (Singleton)")
        return cls._instance

    def get_paths(self) -> tuple[str, str]:
        return self.inventory_file, self.map_file

