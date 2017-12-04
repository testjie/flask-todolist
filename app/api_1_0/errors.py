from app.api_1_0 import bp
from app.utils import code_status
from app.utils.json_utlis import JsonUtils


@bp.app_errorhandler(404)
def page_not_found(e):
    return JsonUtils(msg="404 Not Found", code=404, url="/").get_json()


@bp.app_errorhandler(405)
def page_not_found(e):
    return JsonUtils(msg="405 Method Not Allowed", code=405, url="/").get_json()


@bp.app_errorhandler(500)
def internal_server_error(e):
    return JsonUtils(msg=code_status.ERROR_MSG, code=500).get_json()
