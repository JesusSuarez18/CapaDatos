import logging as log

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa datos.log', encoding='UTF8'),
                    log.StreamHandler()
                ])

if __name__ == '__main__':
    log.debug('Mensaje a nivel de bug')
    log.info('Mensaje a nivel de info')
    log.warning('Mensaje a nivel warning')
    log.error('Mensaje a nivel error')
    log.critical('Mensaje a nivel critico')
