import urllib
def _url(query, page=1, per_page=None, lang='en', filter=True, **kwargs):
    """
    Build google search url with specified query and pagination options.

    :param per_page: 10, 20, 30, 50, 100
    kwargs:
        tbs=qdr:h
        tbs=qdr:d
        tbs=qdr:w
        tbs=qdr:m
        tbs=qdr:y
    """

    if per_page is None:
        per_page = 10
    if isinstance(query, unicode):
        query = query.encode('utf-8')
    start = per_page * (page - 1)
    url = 'http://google.com./search?hl=&tbm=nws&%s&q=%s&start=%s' % (
        lang, urllib.quote(query), start)
    if per_page != 10:
        url += '&num=%d' % per_page
    if not filter:
        url += '&filter=0'
    if kwargs:
        url += '&' + urlencode(kwargs)
    return url
