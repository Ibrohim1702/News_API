from collections import OrderedDict

from base.sqlpaginator import SqlPaginator
from sayt.settings import PER_PAGE
from sayt_api.models import News


def format_news(data):
    return OrderedDict([
        ("id", data.id,),
        ("content", data.content,),
        ('slug', data.slug)
    ])


def paginated_news(requests):
    page = int(requests.GET.get('page', 1))
    ctg = News.objects.all().order_by('-pk')

    limit = PER_PAGE
    offset = (page - 1) * limit

    result = []
    for x in range(offset, offset + limit):
        try:
            result.append(format_news(ctg[x]))
        except:
            break
    pag = SqlPaginator(requests, page=page, per_page=PER_PAGE, count=len(ctg))
    meta = pag.get_paginated_response()

    return OrderedDict([
        ('result', result),
        ('meta', meta)
    ])
