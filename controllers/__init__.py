from app import app

from controllers.index import index_bp
from controllers.users import user_bp
from controllers.ghub import ghub_bp

app.register_blueprint(index_bp)
app.register_blueprint(user_bp)
app.register_blueprint(ghub_bp)
