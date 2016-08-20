from rest_framework.views import APIView
from django.conf import settings
from rest_framework.response import Response
from lily.api.utils import ok, fail


class LilyView(APIView):
    def get(self, request):
        lily = settings.KERNEL
        q = request.GET.get("q", "")
        if q:
            response = lily.respond(q)
            pieces = str.split("::", response)
            action = pieces[0]
            params = pieces[1:]
            return ok(action, params)
        else:
            return fail()
