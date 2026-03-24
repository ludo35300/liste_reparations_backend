from .ocr_controller import ocr_bp
from .reparation_controller import rep_bp
from .stats_controller import stats_bp

def register_blueprints(app):
    app.register_blueprint(ocr_bp,   url_prefix='/api')
    app.register_blueprint(rep_bp,   url_prefix='/api')
    app.register_blueprint(stats_bp, url_prefix='/api')