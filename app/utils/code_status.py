"""
    CODE:返回状态码
"""
FAILED_CODE = 0  # 规则验证不通过
SUCCESS_CODE = 1  # 成功
ERROR_CODE = 10000  # 内部出现错误
PERMISSION_CODE = 20000  # 没有权限

"""
    MSG:返回提示信息
"""
FAILED_MSG = "操作失败，数据为空"
SUCCESS_MSG = "操作成功"
ERROR_MSG = "操作失败，服务内部异常"
PERMISSION_MSG = "登陆状态异常，请重新登陆"
