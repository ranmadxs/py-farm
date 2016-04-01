'''
Created on 30-03-2016

@author: esanchez
'''
import logging

#logging.basicConfig()
log = logging.getLogger("pyfarm")
log.setLevel(logging.DEBUG)


# create console handler and set level to debug
logHandler = logging.StreamHandler()
logHandler.setLevel(logging.DEBUG)

# create formatter
logFormatter = logging.Formatter("%(asctime)s [%(levelname)s]  %(message)s",
                              "%Y-%m-%d %H:%M:%S")
# add formatter to ch
logHandler.setFormatter(logFormatter)

# add handler to logger
log.addHandler(logHandler)

log.info("Init loggin pyfarm")