from rest_framework.views import APIView
from django.conf import settings
from rest_framework.response import Response
from lily.api.utils import ok, fail
import wikipedia


class LilyView(APIView):
    def get(self, request):
        lily = settings.KERNEL
        q = request.GET.get("q", "")
        if q:
            response = lily.respond(q)
            if response:
                pieces = response.split("::")
                action = pieces[0]
                if action == "WIKI_SEARCH":
                    try:
                        wikipedia.set_lang("vi")
                        params = [wikipedia.summary(pieces[1])]
                    except Exception:
                        try:
                            wikipedia.set_lang("en")
                            params = [wikipedia.summary(pieces[1])]
                        except Exception:
                            params = ["Xin lỗi, Tôi chưa được học điều này!"]
                else:
                    params = pieces[1:]
                return ok(action, params)
            else:
                return fail()
        else:
            return fail()
