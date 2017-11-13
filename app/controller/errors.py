from app.controller import bp

@bp.app_errorhandler(404)
def page_not_found(e):
    return "404 not found!",404

@bp.app_errorhandler(500)
def internal_server_error(e):
    return "internal_server_error!",500