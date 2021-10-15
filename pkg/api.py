"""
Api相关定义
"""
class E:
    T = int
    SUCCESS        = 200
    ERROR          = 500
    INVALID_PARAMS = 400

    ERROR_GET_CONTENT       = 10001
    ERROR_CANOT_CLASSIFY    = 10002

DictMsg = {
    E.SUCCESS:                         "ok",
	E.ERROR:                           "fail",
	E.INVALID_PARAMS:                  "请求参数错误",

    E.ERROR_GET_CONTENT:    "抱歉，暂未收录相关信息，不知道如何回复",
    E.ERROR_CANOT_CLASSIFY: "抱歉，暂无法理解您的问题",
}