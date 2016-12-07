from collections import OrderedDict
from rest_framework.response import Response
import wikipedia
from .models import WikiKnowledge, Query

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


def get_wiki(query, lang="vi"):
    wikipedia.set_lang(lang)
    wiki_page = wikipedia.page(query)
    wiki_knowledge = WikiKnowledge.objects.filter(url=wiki_page.url, lang=lang)
    if wiki_knowledge.exists():
        wiki_knowledge = wiki_knowledge.get()
    else:
        wiki_knowledge = WikiKnowledge()
        wiki_knowledge.url = wiki_page.url
        wiki_knowledge.title = wiki_page.title
        wiki_knowledge.content = wiki_page.content
        wiki_knowledge.summary = wiki_page.summary
        wiki_knowledge.lang = lang
        wiki_knowledge.save()
    query_model = Query()
    query_model.name = query
    query_model.wiki = wiki_knowledge
    query_model.save()
    return [wiki_knowledge.summary]
