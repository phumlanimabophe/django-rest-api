from django.urls import get_resolver

def list_urls():
    resolver = get_resolver()
    urls = []
    for url_pattern in resolver.url_patterns:
        urls.append(str(url_pattern.pattern))
    return urls