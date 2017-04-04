from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new_operation/$', views.new_operation, name='new_operation'),
    url(r'^new_category/$', views.new_category, name='new_category'),
    url(r'^new_account/$', views.new_account, name='new_account')
]
