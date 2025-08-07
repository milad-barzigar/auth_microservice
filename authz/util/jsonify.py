from flask import current_app

DEBUG_MSG_CODES = {
    "100": "OK",
    "101": "Unsupported Media Type",
    "102": "Database Error",
    "103": "Resource Not found",
    "104": "Request Validation failed",
    "105": "Empty Data supplied",
    "106": "Resource Expired",
    "107": "Not implemented",
    "108": "Resource expired",
    "109": "Bad Desired Status",
    "110": "Token Encryption Error",
    "111": "Resource Not Matched",
    "112": "Header Not Specified",
    "113": "Token Validation Error",
    "114": "Invalid Token Data",
    "115": "controller Allowed Roles Not Found",
    "116": "Resource Access Denied",
    "117": "Role Not found",
}
def jsonify(state={}, metadata={}, status=200, code=100, headers={}):
    data =state
    data.update(metadata)
    if current_app.debug:
        data["massage"] = DEBUG_MSG_CODES[str(code)]
    data["code"] = code
    return data, status, headers
