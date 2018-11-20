from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from Bookstore.api.resources import BookResource
from django.contrib.auth.views import login, logout
from django.views.generic import TemplateView
from . import views

v1_api = Api(api_name='v1')
v1_api.register(BookResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'NuaaOldBookStore.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),

    # requirement
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/register/$', 'Bookstore.views.register', name='register'),
    url(r'^accounts/$', 'Bookstore.views.account', name='account'),
    url(r'^$', views.home, name='home'),
    url(r'^books/', include('Bookstore.urls')),
    url(r'^help/$', TemplateView.as_view(template_name='help.html'), name='help'),
    url(r'^shopping_cart/', 'Bookstore.views.shopping_cart', name='shopping_cart'),
    url(r'^pay/$', 'Bookstore.views.pay', name='pay'),
    url(r'^comments/commit$', 'Bookstore.views.comments_commit', name='comments_commit'),
    # url(r'^help/$', 'Bookstore.views.help', name='help'),
    url(r'^search/$', 'Bookstore.views.search_page', name='search'),
    url(r'^managebooks/$', 'Bookstore.views.manage_books', name='managebooks'),
)
