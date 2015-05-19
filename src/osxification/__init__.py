import logging

FORMAT = '%(levelname)-8s [%(filename)s %(funcName)s %(lineno)s]: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)
