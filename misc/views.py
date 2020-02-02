from django.core.cache import cache
from django.shortcuts import render
from .models import Page
from guyamoe.settings import STATIC_VERSION
import re


def content(request, page_url):
    page = Page.objects.get(page_url=page_url)
    return render(request, 'misc/misc.html', {'content': page.content, 'template': 'misc_pages_list', "version_query": STATIC_VERSION})

def misc_pages(request):
    pages = cache.get("misc_pages")
    if not pages:
        pages = Page.objects.all().order_by('-date').values_list('page_title', 'page_url')
        cache.set("misc_pages", pages, 3600 * 8)
    return render(request, 'misc/misc_pages.html', {'pages': pages, 'template': 'misc_page', "version_query": STATIC_VERSION})