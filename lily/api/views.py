from rest_framework.views import APIView
from django.conf import settings
from rest_framework.response import Response


class LilyView(APIView):
    def get(self, request):
        lily = settings.KERNEL
        q = request.GET.get("q", "")
        if q:
            return Response(lily.respond(q))
        else:
            return Response("404")
