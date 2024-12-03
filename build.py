from flask_frozen import Freezer
from devserver import app


freezer = Freezer(app)
freezer.freeze()