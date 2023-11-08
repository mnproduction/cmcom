import os
import sys

from cmprj.cmprj.wsgi import application

sys.path.insert(0, os.path.dirname(__file__))

# wsgi = imp.load_source('wsgi', 'passenger_wsgi.py')
# application = wsgi.application

# from cmngr.wsgi import application
