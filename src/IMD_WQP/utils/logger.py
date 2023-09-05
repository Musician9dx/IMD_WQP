import logging as lg
import sys
import os 

lg.basicConfig(
    format='[%(asctime)s : %(levelname)s : %(module)s: %(message)s]',
    level=lg.INFO,
    handlers=[
        lg.FileHandler(os.getcwd()+"/log/logs.log"),
        lg.StreamHandler(sys.stdout)
    ]
)
logger=lg.getLogger('logger')