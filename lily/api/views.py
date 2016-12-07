from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.conf import settings
from lily.api.utils import ok, fail, get_wiki
from .models import Query


class LilyView(APIView):
    # @method_decorator(cache_page(settings.CACHE_TTL))
    def get(self, request):
        lily = settings.KERNEL
        q = request.GET.get("q", "")
        if q:
            response = lily.respond(q)
            if response:
                pieces = response.split("::")
                action = pieces[0]
                if action == "WIKI_SEARCH":
                    pieces[1] = pieces[1].strip()
                    query = Query.objects.filter(name=pieces[1])
                    if query.exists():
                        params = [query.get().wiki.summary]
                    else:
                        try:
                            params = get_wiki(pieces[1], "vi")
                        except Exception:
                            try:
                                params = get_wiki(pieces[1], "en")
                            except Exception:
                                params = ["Xin lỗi, Tôi chưa được học điều này!"]
                else:
                    params = pieces[1:]
                return ok(action, params)
            else:
                return fail()
        else:
            return fail()
