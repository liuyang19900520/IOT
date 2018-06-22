from flask import jsonify


def make_result(data=None, code='0', msg='success'):
    return jsonify({"code": code, "msg": msg, "data": data})
