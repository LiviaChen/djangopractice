from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url('^$', views.frontpage),
    url('^settings$', views.settings),
    url(r'^add_category$', views.addCategory),
    url(r'^delete_category/(?P<category>\w+)', views.deleteCategory),
    url(r'^add_record$', views.addRecord),
    url(r'^delete_record$', views.deleteRecord),
]
