import sys, os, bottle
sys.path = ['/var/www/webdict'] + sys.path

# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))

# ... build or import your bottle application here ...
import webdict # This loads your application

# Do NOT use bottle.run() with mod_wsgi
application = bottle.default_app()
