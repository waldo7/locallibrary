from django.conf import settings
from django.views.static import serve
from django.urls import re_path
import os
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index')
]


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve, {
            'document_root': os.path.join(BASE_DIR, 'catalog/static'),
        }),
    ]
