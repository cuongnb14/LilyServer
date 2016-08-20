from collections import OrderedDict
from rest_framework.response import Response


def ok(action, params):
    msg = OrderedDict()
    msg["status"] = "OK"
    msg["action"] = action
    msg["params"] = params
    return Response(msg)


def fail():
    msg = OrderedDict()
    msg["status"] = "ERROR"
    return Response(msg)
