from Conexion.logger_base import log
from Conexion.conexion import Conexion


class CursorDelPool:

    def __int__(self, conexion=None, cursor=None):
        self._conexion = conexion
        self._cursor = cursor

    def __enter__(self):
        log.debug(f'Inicio del método with __enter__')
        self._conexion = Conexion.obtener_conexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipo_excepcion, valor_excepción, detalle_excepcion):
        log.debug(f'Se ejecuta metodo exit')
        if valor_excepción:
            self._conexion.rollback()
            log.error(
                f'Ocurrió una excepcion de tipo, se realiza un rollback :{valor_excepción} {tipo_excepcion} {detalle_excepcion}')
        else:
            self._conexion.commit()
            log.debug(f'Commit de la transacción')
        self._cursor.close()
        Conexion.liberar_conexion(self._conexion)


if __name__ == '__main__':
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM persona')
        log.debug(cursor.fetchall())
