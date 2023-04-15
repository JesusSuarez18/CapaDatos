from Conexion.logger_base import log
from psycopg2 import pool
import sys


class Conexion:
    _DATABASE = '*******'
    _USERNAME = '********'
    _PASSWORD = '************'
    _DB_PORT = '****'
    _HOST = '*********'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtener_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      database=cls._DATABASE)
                log.debug(f'Creacion del pool de manera exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.debug(f'Ocurrio un error al obtener el pool -> {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtener_conexion(cls):
        conexion = cls.obtener_pool().getconn()
        log.debug(f'Conexion obtenida del pool {conexion}')
        return conexion

    @classmethod
    def liberar_conexion(cls, conexion):
        cls.obtener_pool().putconn(conexion)
        log.debug(f'Regresamos la conexión al pool: {conexion}')

    @classmethod
    def cerrar_conexiones(cls):
        cls.obtener_pool().closeall()


if __name__ == '__main__':
    conexion1 = Conexion.obtener_conexion()
    Conexion.liberar_conexion(conexion1)
    conexion2 = Conexion.obtener_conexion()
    conexion3 = Conexion.obtener_conexion()
    Conexion.liberar_conexion(conexion3)
    conexion4 = Conexion.obtener_conexion()
    conexion5 = Conexion.obtener_conexion()
    Conexion.liberar_conexion(conexion5)
